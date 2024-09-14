const express = require("express");
const app = express();
const port = 80;

// Serve static directory
app.use(express.static("static"));

app.get("/api/oath", (req, res) => {});

app.listen(port);
