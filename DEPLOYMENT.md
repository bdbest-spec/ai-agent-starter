# Deployment

This repository is ready to deploy as a Docker web service on [Render](https://render.com/).

## Deploy in a few minutes

1. Push this repository to GitHub (already done for this project).
2. In Render, choose **New + → Blueprint** and select `bdbest-spec/ai-agent-starter`.
3. Render will read `render.yaml` and create the `amanah-ethos-ai` web service.
4. Add your `OPENAI_API_KEY` as a secret when prompted. Never commit the key to Git.
5. Wait for the deploy to finish, then open the generated `onrender.com` URL.
6. Verify the service at `/health`; it should return `{"status":"ok"}`.

The service listens on Render's `$PORT`, serves the web UI at `/`, and exposes the API at `/chat`.

## Important production checklist

- Add an OpenAI billing limit and monitor usage.
- Keep `OPENAI_API_KEY` in Render's environment settings only.
- Add authentication and rate limiting before sharing the URL publicly.
- Review logs and configure a custom domain if desired.

The app cannot be deployed from GitHub alone: a hosting account and an API key are required. The files in this repository remove the server-configuration work so the remaining step is connecting the repository to a host such as Render.
