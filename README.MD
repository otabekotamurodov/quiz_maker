```
quiz_bot/
│
├── bot/
│   ├── main.py              # bot entry
│   ├── handlers/
│   │   ├── start.py
│   │   ├── file_upload.py
│   │   └── quiz_response.py
│
├── services/
│   ├── file_parser.py       # PDF/DOCX/TXT
│   ├── text_cleaner.py
│   ├── quiz_generator.py    # OpenAI bilan ishlaydi
│
├── prompts/
│   └── quiz_prompt.txt
│
├── config.py
├── requirements.txt
└── README.md

```