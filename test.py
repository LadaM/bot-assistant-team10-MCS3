import textwrap

note_text = "Це є деякий дуже довгий текст, який потрібно обрізати."
note_width = 20
ellipsis = "..."
note_text_formatted = textwrap.shorten(
    note_text, width=note_width, placeholder=ellipsis
)

print(note_text_formatted)
