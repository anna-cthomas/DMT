const express = require("express");
const app = express();
const port = 80;

// Serve static directory
app.use(express.static("static"));

app.get("/api/oath", (_req, _res) => {});

app.listen(port);
