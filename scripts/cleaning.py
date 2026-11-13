"""Reconstruct frozen cleaning flags from source flags and recorded identities."""
def reconstruct(rows,duplicate_mapping):
    mappings={(m['corpus'],m['source_record_id']):m for m in duplicate_mapping}
    out=[]
    for source in rows:
        r=dict(source);r['is_duplicate']=r['original_is_duplicate'];r['year']=r['original_year']
        r['analysis_record_id']=None if r['is_duplicate'] or r['insufficient_abstract'] else r['record_id']
        r['cleaning_exclusion_reason']='source_duplicate_flag' if r['is_duplicate'] else 'insufficient_abstract' if r['insufficient_abstract'] else None
        m=mappings.get((r['corpus'],r['record_id']))
        if m:
            r['analysis_record_id']=m['analysis_record_id']
            if not m['retained']:
                r['is_duplicate']=True;r['cleaning_exclusion_reason']='additional_bibliographic_duplicate'
            else:r['year']=m['analysis_year']
        out.append(r)
    return out
