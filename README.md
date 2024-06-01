# SynapseFlow-Backend
**RESTful API** for the [SynapseFlow](https://synapseflow.vercel.app/) website.

## Getting Started 🚀
### Prerequisites ⚙️
- Installed **Docker Compose** (install one if haven't already) [Installation Guide](https://docs.docker.com/compose/install/)

### Installation 🔧
1. Copy the repository:
    `git clone https://github.com/Kumala3/SynapseFlow-Backend.git`

2. Change `.env.dist` to `.env` and fill in with your own credentials

3. Run the project:
    - **In production**:
        `docker compose -f docker-compose.prod.yml up --build`
    - **In development**:
        `docker compose -f docker-compose.dev.yml up --build`
