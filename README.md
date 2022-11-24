## Gouach Challenge
   [![Gouach Challenge][product-screenshot]](https://gouach.com)

## Tech design

### Built With

* Python3 (Flask / [dnslib](https://github.com/paulc/dnslib)) for the API and the DNS Server
* Javascript (NuxtJS) for the dashboard
* Redis for the persistence
* Docker to run the local stack

### Tech Design Diagram

   [![Gouach Challenge][tech-screenshot]](https://gouach.com)

### Tech Appraoch
[Here you will find a few words regarding how I've approched the challenge](https://github.com/camgrsl/gouach-challenge/blob/main/APPROACH.md)

## Getting Started

### Prerequisites

* docker
* makefile

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:camgrsl/gouach-challenge.git
   ```
2. Build the stack
   ```sh
   make up
   ```
3. Fill the server with mocked data
   ```sh
   make mock-data
   ```
4. The `make up` command run the compose in attached mode, so you should see the dns server printing the ouputs straight in your terminal.

## Usage

- API URL: http://localhost:3000
- Dashboard: http://localhost:3001

[tech-screenshot]: tech-design.png
[product-screenshot]: preview.png
