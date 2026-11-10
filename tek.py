FONT = "'Segoe UI',Arial,sans-serif"
baris1 = ["Java", "JavaScript", "TypeScript", "Python", "HTML5", "CSS3", "React", "Next.js", "Vite", "Tailwind CSS", "Three.js", "PWA", "Node.js", "Express", "Hono"]
baris2 = ["MySQL", "PostgreSQL", "SQLite", "Prisma", "Hibernate", "Supabase", "Firebase", "Cloudflare Workers", "Cloudflare Pages", "D1", "Workers AI", "Netlify",
          "pandas", "NumPy", "scikit-learn", "Streamlit", "OpenCV", "Git", "Maven", "JasperReports", "Playwright"]


def chips(daftar):
    x, out = 0, ""
    for n in daftar:
        w = int(len(n) * 11.2 + 52)
        out += (f'<g><rect x="{x}" y="0" width="{w}" height="54" rx="27" fill="#18181b" stroke="#52525b" stroke-width="1.4"/>'
                f'<circle cx="{x + 24}" cy="27" r="4.2" fill="#d4d4d8"/>'
                f'<text x="{x + 38}" y="34" fill="#f4f4f5" font-family="{FONT}" font-size="20" font-weight="500">{n}</text></g>\n')
        x += w + 16
    return out, x


c1, w1 = chips(baris1)
c2, w2 = chips(baris2)
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="190" viewBox="0 0 1200 190" role="img" aria-label="Teknologi yang saya pakai">
<defs>
<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.07" stop-color="#fff"/><stop offset="0.93" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="m"><rect width="1200" height="190" fill="url(#fade)"/></mask>
</defs>
<style>
.a{{animation:kiri {max(int(w1 / 55), 12)}s linear infinite}}
.b{{animation:kanan {max(int(w2 / 55), 12)}s linear infinite}}
@keyframes kiri{{from{{transform:translateX(0)}}to{{transform:translateX(-{w1}px)}}}}
@keyframes kanan{{from{{transform:translateX(-{w2}px)}}to{{transform:translateX(0)}}}}
</style>
<g mask="url(#m)">
<g transform="translate(0,14)"><g class="a">{c1}<g transform="translate({w1},0)">{c1}</g><g transform="translate({2 * w1},0)">{c1}</g></g></g>
<g transform="translate(0,104)"><g class="b">{c2}<g transform="translate({w2},0)">{c2}</g><g transform="translate({2 * w2},0)">{c2}</g></g></g>
</g></svg>"""
open("assets/teknologi-bergerak.svg", "w", encoding="utf-8", newline="\n").write(svg)
print(w1, w2)
