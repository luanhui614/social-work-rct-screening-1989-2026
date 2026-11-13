/** Render Supplementary Figure S1 from frozen workflow counts using D3 + Playwright.
 * Optional graphics dependencies: npm install d3 playwright
 * Supply CHROME_PATH if using an existing Chrome executable.
 * D3_PATH and PLAYWRIGHT_MODULE may identify existing dependency installations.
 * The numerical analysis and its CI do not require these graphics dependencies.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const data=JSON.parse(fs.readFileSync(path.join(root,'figures/source_data/Figure_S1.json'),'utf8'));
const {chromium}=process.env.PLAYWRIGHT_MODULE ? await import(process.env.PLAYWRIGHT_MODULE) : await import('playwright');
const d3Path=process.env.D3_PATH || path.resolve(path.dirname(require.resolve('d3')),'../dist/d3.min.js');
const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{}),args:['--no-sandbox']});
try {
 const page=await browser.newPage({viewport:{width:1000,height:1224},deviceScaleFactor:2});
 await page.setContent('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:white}svg{display:block}text{font-family:Arial,Helvetica,sans-serif;fill:#202020}</style></head><body><div id="chart"></div></body></html>');
 await page.addScriptTag({content:fs.readFileSync(d3Path,'utf8')});
 await page.evaluate(d=>{
  const W=1000,H=1224,M=26,G=24;
  const half=(W-2*M-G)/2,third=(W-2*M-2*G)/3;
  const y=[58,162,296,390,486,598,854,984,1102];
  const x=(n,i)=>M+i*((W-2*M-(n-1)*G)/n+G);
  const svg=d3.select('#chart').append('svg').attr('xmlns','http://www.w3.org/2000/svg').attr('width',W).attr('height',H).attr('data-figure','S1');
  svg.append('defs').append('marker').attr('id','arrow').attr('viewBox','0 -5 10 10').attr('refX',9).attr('refY',0).attr('markerWidth',7).attr('markerHeight',7).attr('orient','auto').append('path').attr('d','M0,-5L10,0L0,5').attr('fill','#444');
  const f=n=>d3.format(',')(n),j=d.journal,c=d.conference;
  svg.append('text').attr('data-title','workflow').attr('x',W/2).attr('y',M+4).attr('text-anchor','middle').attr('font-size',25).attr('font-weight',700).text(d.title);
  function box(id,xx,yy,w,h,lines,fill='#f7f7f7'){
   const g=svg.append('g').attr('data-node',id);
   g.append('rect').attr('x',xx).attr('y',yy).attr('width',w).attr('height',h).attr('rx',4).attr('fill',fill).attr('stroke','#555').attr('stroke-width',1.2);
   const leading=25,start=yy+h/2-(lines.length-1)*leading/2+7;
   lines.forEach((t,i)=>g.append('text').attr('data-label',id+'-'+i).attr('x',xx+w/2).attr('y',start+i*leading).attr('text-anchor','middle').attr('font-size',i?19:20).attr('font-weight',i?400:700).text(t));
   return {id,x:xx,y:yy,w,h};
  }
  function arrow(a,b,ax=a.x+a.w/2,bx=b.x+b.w/2,label=''){
   const sy=a.y+a.h,ey=b.y,mid=(sy+ey)/2;
   svg.append('path').attr('data-edge',a.id+'-'+b.id).attr('d',`M${ax},${sy}V${mid}H${bx}V${ey-2}`).attr('fill','none').attr('stroke','#444').attr('stroke-width',1.5).attr('marker-end','url(#arrow)');
   if(label)svg.append('text').attr('data-edge-label',a.id+'-'+b.id).attr('x',bx+8).attr('y',mid+18).attr('font-size',16).text(label);
  }
  const rawJ=box('journal-source',x(2,0),y[0],half,76,['Journal source records',f(j.raw_records)+' | 88 journals | 1989–2025']);
  const rawC=box('conference-source',x(2,1),y[0],half,76,['Conference source records',f(c.raw_records)+' | 22 programs | 2005–2026']);
  const clJ=box('journal-cleaning',x(2,0),y[1],half,106,['Data cleaning',f(j.total_duplicate_records)+' duplicate indices excluded','After deduplication: '+f(j.records_after_deduplication),f(j.insufficient_abstract_records)+' insufficient abstract excluded']);
  const clC=box('conference-cleaning',x(2,1),y[1],half,106,['Data cleaning',f(c.total_duplicate_records)+' duplicate indices excluded','After deduplication: '+f(c.records_after_deduplication),'No insufficient abstract exclusions']);
  const elJ=box('journal-eligible',x(2,0),y[2],half,64,['Eligible journal records','J = '+f(j.clean_eligible_records)]);
  const elC=box('conference-eligible',x(2,1),y[2],half,64,['Eligible conference abstracts','C = '+f(c.clean_eligible_records)]);
  arrow(rawJ,clJ);arrow(rawC,clC);arrow(clJ,elJ);arrow(clC,elC);
  const model=box('retained-model-results',M,y[3],W-2*M,66,['Dual-model title and abstract screening','Same codebook and seven labels; INDIVIDUAL or CLUSTER = RCT']);
  arrow(elJ,model,elJ.x+half/2,elJ.x+half/2);arrow(elC,model,elC.x+half/2,elC.x+half/2);
  const specs=[['concordant_positive','Both classify as RCT'],['discordant','One classifies as RCT'],['concordant_negative','Both classify as non-RCT']];
  const groups=specs.map(([key,title],i)=>box(key,x(3,i),y[4],third,82,[title,'J = '+f(j.clean_model_groups[key]),'C = '+f(c.clean_model_groups[key])]));
  groups.forEach(g=>arrow(model,g,g.x+third/2));
  const q=(cor,key)=>cor.verification_by_group.find(r=>r.stratum===key);
  const pj=q(j,'concordant_positive'),pc=q(c,'concordant_positive'),dj=q(j,'discordant'),dc=q(c,'discordant'),nj=q(j,'concordant_negative'),nc=q(c,'concordant_negative');
  const positives=box('verify-positive',x(3,0),y[5],third,208,['Human verification: all',`J: ${f(pj.classifiable_deduplicated)} reviewed`,`${pj.rct} RCT; ${pj.non_rct} non-RCT`,`C: ${f(pc.classifiable_deduplicated)} reviewed`,`${pc.rct} RCT; ${pc.non_rct} non-RCT`]);
  const disagreements=box('verify-disagreement',x(3,1),y[5],third,208,['Human review: all',`J: ${f(dj.classifiable_deduplicated)} reviewed`,`${dj.rct} RCT; ${dj.non_rct} non-RCT`,`C: ${f(dc.classifiable_deduplicated)} reviewed`,`${dc.rct} RCT; ${dc.non_rct} non-RCT`]);
  const negatives=box('verify-negative',x(3,2),y[5],third,208,['Targeted human sample','Score / keyword candidate pools',`J ${nj.classifiable_deduplicated}: ${nj.rct} RCT; ${nj.non_rct} non-RCT`,`C ${nc.classifiable_deduplicated}: ${nc.rct} RCT; ${nc.non_rct} non-RCT`,'Additional review: J 1 non-RCT','Unreviewed remain excluded:',`J ${f(j.unreviewed_concordant_negatives)}; C ${f(c.unreviewed_concordant_negatives)}`]);
  [positives,disagreements,negatives].forEach((g,i)=>arrow(groups[i],g));
  const final=box('final-rct-reports',M,y[6],W-2*M,98,['Final human-confirmed RCT reports',`J: ${pj.rct} + ${dj.rct} + ${nj.rct} = ${j.final_rct_reports} / ${f(j.clean_eligible_records)} eligible records`,`C: ${pc.rct} + ${dc.rct} + ${nc.rct} = ${c.final_rct_reports} / ${f(c.clean_eligible_records)} eligible abstracts`],'#ededed');
  [positives,disagreements,negatives].forEach(g=>arrow(g,final,g.x+g.w/2,g.x+g.w/2,'RCTs'));
  const desc=box('descriptive-analysis',x(2,0),y[7],half,88,['Descriptive analyses and rates','Overall, annual, period, journal and format','Use all eligible records as denominators']);
  const link=box('record-linkage',x(2,1),y[7],half,88,['Conference–journal linkage',`${c.final_rct_reports} eligible conference reports`,'against all '+f(j.clean_eligible_records)+' eligible journal records']);
  arrow(final,desc,desc.x+half/2,desc.x+half/2);arrow(final,link,link.x+half/2,link.x+half/2);
  const notes=[`Verification source worklist: ${f(d.original_worklist_n)}; after cleaning: ${f(d.clean_verification_n)} (J ${j.unique_classifiable_verification_records}; C ${c.unique_classifiable_verification_records}). Disputed cases received author adjudication.`, 'The additional journal non-RCT is outside that sample. J = journal records; C = conference abstracts.', 'This is the final analytical data flow; original model calls covered the complete source extracts.', 'Targeted negative-sample verification does not estimate whole-pool sensitivity or NPV.'];
  notes.forEach((t,i)=>svg.append('text').attr('data-note','workflow-'+i).attr('x',M).attr('y',y[8]+i*25).attr('font-size',17).text(t));
 },data);
 await page.evaluate(()=>document.fonts.ready);
 const svg=await page.locator('svg').evaluate(el=>el.outerHTML);
 fs.writeFileSync(path.join(root,'figures/Figure_S1.svg'),svg+'\n');
 await page.locator('svg').screenshot({path:path.join(root,'figures/Figure_S1.png')});
 await page.pdf({path:path.join(root,'figures/Figure_S1.pdf'),width:'1000px',height:'1224px',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
 console.log('Rendered Figure S1 as SVG, PNG and PDF from frozen workflow counts.');
} finally {await browser.close();}
