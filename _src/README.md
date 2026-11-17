# Source for the St Leonards info day pages

The published pages (index.html and the language folders) are generated from these files.

- `langs/en.json` – English text. `langs/b*.json` – translations (27 languages).
- `template.html` – page template with `{{placeholders}}`.
- `build.py` – builds every language page: `python3 build.py ..` (run inside `_src`, writes to the repo root).
- `zoom.json` – print scale per language so each prints on one A4 page.

To change the info day date or time, update `date_heading`, `cal_*`, `time`, `s1_d` and `meta_desc` in every language file, then rebuild.

## Enquiry form
The form posts to FormSubmit (https://formsubmit.co), which emails each enquiry to
esolstleonards@tafensw.edu.au. To change the address, replace it in `form_patch.py`
(two places), run `make_template.py`, then rebuild. Form text is in `langs/en.json`
and `langs/f_form_*.json`.
