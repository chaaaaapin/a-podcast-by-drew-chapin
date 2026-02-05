# a podcast by drew chapin

**URL:** https://apodcastbydrewchapin.com
**Status:** Pre-launch landing page
**Tech Stack:** Static HTML/CSS/JS + Ghost newsletter integration

## Overview

Simple landing page for Drew Chapin's upcoming podcast. Features animated gradient background, email signup form connected to the chapin.io Ghost newsletter, and proper schema markup for podcast SEO.

## Design

- **Gradient:** Animated left-right gradient (#BECC41 lime green → #189BCC bright blue)
- **Typography:** Avenir font family
- **Layout:** Center-aligned with three rows:
  1. Large "a podcast" heading (50% screen height)
  2. Smaller "by drew chapin" byline
  3. Email signup form

## Ghost Integration

Newsletter signup connects to the Ghost installation at **chapin.io**. The form uses Ghost's standard `data-members-form` attributes and loads the Ghost Portal script from chapin.io.

When users submit their email:
1. Ghost sends a magic link to their email
2. User clicks link to confirm subscription
3. They're added to the chapin.io newsletter list

## Schema Markup

Includes `PodcastSeries` schema with:
- Show name and description
- Host/author information (Drew Chapin)
- sameAs links to Drew's profiles (drewchapin.com, chapin.io, LinkedIn, Instagram/Threads, GitHub, Bluesky)
- Genre tags (Business, Technology, Entrepreneurship)

## Files

- `index.html` — Landing page
- `llms.txt` — LLM-readable show description and host bio
- `README.md` — This file

## Deployment

Deploy to **Cloudflare Pages**:

1. Push to GitHub repo (or use direct upload)
2. Connect to Cloudflare Pages
3. Build settings:
   - Framework preset: None (static HTML)
   - Build command: (none)
   - Build output directory: `/`
4. Point `apodcastbydrewchapin.com` DNS to Cloudflare Pages

## Domain Setup

Domain registered, needs DNS configuration:
- Add CNAME record pointing to Cloudflare Pages deployment
- Enable HTTPS (auto via Cloudflare)

## Future Enhancements

When podcast launches:
- Add podcast feed URL to schema
- Link to episode pages
- Add RSS feed link
- Update schema from `PodcastSeries` to include `PodcastEpisode` items

---

**Created:** February 5, 2026
**Last Updated:** February 5, 2026
