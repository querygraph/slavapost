# SlavaPost

Turn Slava Tykhonov's public LinkedIn newsletter editions into `.textpack`
archives that import directly into Omnighost (and Ulysses).

## From an iPhone

1. Open **Actions → Import LinkedIn post → Run workflow**.
2. Paste a public LinkedIn article URL into `post_url`.
3. Tap **Run workflow**.
4. Download the `.textpack` from the run's **Artifacts** section.

The workflow also commits the canonical Markdown, downloaded images, metadata,
and TextPack to `posts/<slug>/`, then creates or updates the Ghost post by slug.
Immediate publication is the default; choose `draft` in the run form when
review is desirable.

## Automatic newsletter check

`Check Slava newsletter` runs daily and follows article links discoverable from
the configured seed edition. If it finds an edition not already under `posts/`,
it imports, publishes, and commits it. Its default status is controlled by
`publish_status` in `config.json`.

Direct publication requires repository Actions secrets named
`GHOST_ADMIN_URL` and `GHOST_ADMIN_API_KEY`.

LinkedIn sometimes changes its public HTML or blocks unattended requests. A
blocked fetch fails visibly instead of creating a partial post; paste the URL
into the manual workflow and retry later.

## Omnighost format

Each archive is a zipped TextBundle:

```text
<slug>.textbundle/
  text.markdown
  info.json
  assets/*
```

`info.json` contains TextBundle v2 fields plus Omnighost metadata. By default
the destination blog is `querygraph.ai`; override it in the manual workflow.

## Local use

```bash
python -m pip install -r requirements.txt
python scripts/linkedin_textpack.py \
  "https://www.linkedin.com/pulse/..." \
  --blog querygraph.ai
```

The importer only reads public pages. It does not store LinkedIn cookies,
passwords, or session tokens.
