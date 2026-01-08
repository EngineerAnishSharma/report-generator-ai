Vision-Language Report Generator
=================================

Overview
--------
Small FastAPI app that analyzes CSVs and images and generates business reports using OpenAI and local image models.

Quick Start (local)
-------------------
Prereqs:
- Python 3.11
- pip

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create environment variables (see `.env.example`)

3. Run locally (dev)

```bash
uvicorn app.main:app --reload
```

Production start commands
-------------------------
- Use Procfile (recommended for Render): the Procfile contains `web: uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
- Or explicit commands:

Dev (hot-reload):
```bash
uvicorn app.main:app --reload
```

Production (recommended):
```bash
# install gunicorn then run
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

Environment Variables
---------------------
Required:
- `DATABASE_URL` — PostgreSQL connection string (e.g. `postgresql://user:pass@host:5432/dbname`)
- `OPENAI_API_KEY` — OpenAI API key for report generation

Optional (only if used):
- `QDRANT_HOST`, `QDRANT_PORT`, `QDRANT_API_KEY`
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_BUCKET`, `AWS_REGION`

`.env` example is provided in `.env.example`.

Deploying to Render
-------------------
1. Create a Render account and connect your GitHub repo.
2. Click New → Web Service and choose this repo.
3. Branch: `master` (or your preferred branch).
4. Leave Build and Start commands blank so Render uses the `Procfile`.
5. Add environment variables in the Render dashboard (`DATABASE_URL`, `OPENAI_API_KEY`, etc.).
6. (Optional) Create a managed PostgreSQL on Render and paste its `DATABASE_URL` into the service env vars.
7. Create the service and monitor build logs. The app will be available at the provided URL; API docs at `/docs`.

Testing & Troubleshooting
-------------------------
- Check `/docs` for interactive API docs.
- Use the Render service logs for build/runtime errors.
- Locally, run `uvicorn app.main:app --reload` and watch stdout for errors.

Commit & Push
-------------
After reviewing, commit the README and push:

```bash
git add README.md
git commit -m "Add README with setup and deployment instructions"
git push origin master
```

Need help automating the commit/push or adjusting the Procfile/start command? Tell me which option you prefer and I will apply it.
