# Post-Mortem Hallucination Audit Checklist

Run this before you publish, or forever be haunted by red diff circles on Twitter.

1. **Source Tag Rule** → Every factual sentence gets a superscript citation[^1]  
   No tag → delete or rephrase as "believed to be"

2. **Numeric Guardrails** → Any number must be triangulated or flagged  
   Good: ~2× larger than normal[^2]  
   Bad: 1.8 GB (unless vendor literally said it)

3. **Code Path Hygiene** → No fake filenames/functions  
   Allowed: dge config loader (exact path redacted)

4. **Timeline Sanity** → Minute-level only if published  
   Good: egan ~11:20 UTC

5. **Uncertainty Footnote Section** (mandatory)
   ### Known Unknowns & Inferences
   - Exact file size: Vendor said "doubled", no absolute disclosed
   - Crash reason: Inferred from Rust + size limit pattern

6. **Final Red-Team Sign-off**  
   Paste draft into #incidents with: "Spot the hallucination – first correct flag gets a cookie 🍪"
