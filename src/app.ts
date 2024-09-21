import { Client } from "twitter-api-sdk";
import * as dotenv from "dotenv";
import express from "express";

// Variables
const app = express();
const port = 80;

dotenv.config();

const client = new Client(process.env.BEARER_TOKEN as string, );
const { data } = await client.users.findUserByUsername("gilgameshxzero");
if (!data) throw new Error("Couldn't find user");
let count = 0;
for await (const followers of client.users.usersIdFollowers(data.id)) {
	console.log(followers);
	if (++count == 15) {
		break;
	}
}

// Serve static directory
app.use(express.static("static"));

// Listen for any incoming requests
app.listen(port);
