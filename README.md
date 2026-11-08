<div align="center">

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/banner-dark.svg" alt="Oleksii Iovchev — Backend Lead · Python · Distributed systems · a bit of Rust" width="100%">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=2800&pause=1200&color=A78BFA&center=true&vCenter=true&width=620&height=44&lines=Backend+Lead+%C2%B7+5%2B+years+in+production;Async+Python+%C2%B7+distributed+systems;Queues%2C+retries+and+idempotency;Observability+and+load+testing;Learning+a+bit+of+Rust+%F0%9F%A6%80" alt="Backend Lead · 5+ years in production · Async Python · distributed systems">

<p>
  <img src="https://img.shields.io/badge/coffee-4%2C812%20cups-7c3aed?style=flat-square&labelColor=1f2937" alt="coffee: 4,812 cups">
  <img src="https://img.shields.io/badge/git%20push%20--force-0%20times-0891b2?style=flat-square&labelColor=1f2937&logo=git&logoColor=white" alt="git push --force: 0 times">
  <img src="https://img.shields.io/badge/naming%20things-37%25%20of%20the%20time-7c3aed?style=flat-square&labelColor=1f2937" alt="naming things: 37% of the time">
</p>

</div>

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/divider-dark.svg" alt="" width="100%">

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/flow-dark.svg" align="right" width="34%" alt="A request goes through the API and a queue to a worker: at-least-once delivery with retries, and an idempotent write to the database">

```python
class BackendEngineer:
    name = "Oleksii Iovchev"
    role = "Backend Lead"
    experience = "5+ years"
    focus = [
        "system design",
        "distributed systems",
        "production reliability",
    ]
    learning = "Rust"
    speaks = ["EN", "UA", "FR"]
    max_retries = 3  # the fourth one is a postmortem

    def introduce(self) -> str:  # idempotent: safe to retry
        return (
            f"Hi, I'm {self.name}, {self.role.lower()}.\n"
            "I build async services and message-driven\n"
            "workflows that stay boring in production."
        )


print(BackendEngineer().introduce())
```

<br clear="right">

<p align="center">
  <img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/terminal-dark.svg" alt="$ python whoami.py — Hi, I'm Oleksii Iovchev, backend lead. I build async services and message-driven workflows that stay boring in production." width="720">
</p>

### 🛠️ What I do

- 🧭 **Lead the backend of a product team**: architecture, code review, task breakdown, owning production
- ⚙️ **Async Python services**: APIs, background workers, message-driven workflows, idempotent processing
- 📈 **Reliability**: metrics, logs and alerts, load testing with k6, safe migrations and rollouts
- 🧠 **LLM and RAG pipelines**: retrieval, structured outputs, tool-calling agents over MCP
- 🦀 **A bit of Rust**: a low-latency networking side project (UDP, gRPC, Linux tuning)

> I like systems you can reason about in the middle of an incident: explicit state, idempotent steps,
> and metrics that answer the question before anyone has to ask it.

**Currently curious about:** tail latency, backpressure, and how far Rust can push a single core.

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/divider-dark.svg" alt="" width="100%">

<h3 align="center">🧰 Tech stack</h3>

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,fastapi,django,postgres,mysql,mongodb,redis,elasticsearch,rabbitmq&theme=dark" alt="Python, FastAPI, Django, PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch, RabbitMQ">
  <br>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,aws,cloudflare,nginx,linux,prometheus,grafana,gitlab&theme=dark" alt="Docker, Kubernetes, AWS, Cloudflare, Nginx, Linux, Prometheus, Grafana, GitLab">
  <br>
  <img src="https://skillicons.dev/icons?i=rust,js,githubactions,git,bash,selenium&theme=dark" alt="Rust, JavaScript, GitHub Actions, Git, Bash, Selenium">
</p>

<p align="center">
  <sub><b>also</b> · SQLAlchemy · Alembic · Pydantic · asyncio · Celery · NATS · Helm · Loki · k6 · LangChain · LangGraph · MCP · Qdrant · gRPC · Playwright · uv · ruff · pytest</sub>
</p>

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/divider-dark.svg" alt="" width="100%">

<h3 align="center">📦 Selected projects</h3>

<p align="center">
  <a href="https://github.com/alekseyiovchev/cef-syslog-udp-proxy"><img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/card-cef-syslog-udp-proxy-dark.svg" alt="cef-syslog-udp-proxy: async UDP proxy for CEF/Syslog events" width="400"></a>
  <a href="https://github.com/alekseyiovchev/rag-document-search-api"><img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/card-rag-document-search-api-dark.svg" alt="rag-document-search-api: RAG service over Qdrant" width="400"></a>
  <a href="https://github.com/alekseyiovchev/csv-worker-api"><img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/card-csv-worker-api-dark.svg" alt="csv-worker-api: background CSV processing with Celery" width="400"></a>
</p>

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/divider-dark.svg" alt="" width="100%">

<h3 align="center">⚡ At a glance</h3>

<p align="center">
  <img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/languages-dark.svg" alt="Languages: Python 75%, JavaScript 15%, Rust 10%" width="400">
  <img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/status-dark.svg" alt="Status: idempotent handlers and observability operational, migrations forward-only, load tests passing, Rust learning, Friday deploys disabled" width="400">
</p>

<img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/divider-dark.svg" alt="" width="100%">

<p align="center">
  <img src="https://raw.githubusercontent.com/alekseyiovchev/alekseyiovchev/main/assets/snake-dark.svg" alt="A snake eating my contribution graph" width="100%">
</p>

<h3 align="center">🤝 Connect</h3>

<p align="center">
  <a href="https://www.linkedin.com/in/alekseyiovchev/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

<p align="center"><sub>Built with ☕ and asyncio</sub></p>
