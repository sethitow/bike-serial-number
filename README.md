# Bike Serial Number Tool

- [Application](http://serialnumber.sethitow.com)
- [Repository](https://github.com/sethitow/bike-serial-number)
- [Continuous Integration](https://gitlab.com/sethitow/bike-serial-number/-/pipelines)

## Overview
### Backend
The backend is a Python web service using the Flask microframework. It provides a GraphQL endpoint at `/graphql`.

The service implements the following schema:
```
schema {
  query: Query
}

type Bike {
  model: String
  modelYear: Int
  manufactureMonth: Int
  manufactureYear: Int
  factory: String
  version: Int
  serialNumber: Int
}

input BikeInput {
  model: String!
  modelYear: Int!
  manufactureMonth: Int!
  manufactureYear: Int!
  factory: String!
  version: Int!
  serialNumber: Int!
}

type Query {
  bikeInfo(serialCode: String!): Bike
  bikeSerialCode(bike: BikeInput): String
}
```

Unit tests are written for the core logic that parses serial numbers. 

### Frontend
The frontend is a React app using the Material-UI component library. It talks to the backend using the Apollo GraphQL client.

In production, the frontend is served by a stateless Nginx container. 

### CI and Deployment
The frontend and backend are containerized using Docker. A continuous integration pipeline runs on each push through Gitlab. The containers are build by GitLab and are pushed to the GitLab container registry. 

The application is deployed onto a Kubernetes cluster. The frontend and backend are separate services so they can be scaled independently. Kubernetes provides an ingress resource which acts as a reverse proxy to route traffic to the correct service. SSL/TLS is provisioned using LetsEncrypt. 

## Todo
This application was created as a demonstration in a limited amount of time. There are many places for improvement.

### Form to encode a new Serial Code
The server provided facilities to encode a new serial code given a set of bike facts. The UI does not currently expose this in any way. A form could be created to allow the user to create a new serial code.

### Authentication
Authorization currently consists of a hardcoded bearer token that is checked by the server. This could be expanded to use a single sign-on provider.
