const express = require("express");
const cors = require("cors");
const app = express();
const fs = require("fs");
const http = require("http");
const url = require("url");
const { stringify } = require("querystring");
const fetch = (...args) =>
    import("node-fetch").then(({ default: fetch }) => fetch(...args));
  
// const file = "D:\\GitHub\\Sleep_Data_Visualization\\SDV.json";
// const file = "https:\\\\github.com\\ccy05327\\Sleep-Data-Visualization\\blob\\main\\SDV.json";
const file = "https:\\ccy05327.github.io\\Sleep-Data-Visualization\\SDV.json";
// const file = "https://raw.githubusercontent.com/ccy05327/Sleep-Data-Visualization/main/SDV.json";
// D:\GitHub\SDV-API\index.js

const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

/** Return array of records according to input parameter int */
function past_record(n) {
  data = JSON.stringify(data[0].slice(-n - 2, -2));
  return data;
}


// https://nodejs.org/en/knowledge/HTTP/clients/how-to-access-query-string-parameters/
http
  .createServer((req, res) => {
    const queryObject = url.parse(req.url, true).query;
    // console.log(queryObject);
    res.writeHead(200, {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      "X-Powered-By": "nodejs",
    });
    if ("past" in queryObject) {
      fetch(file)
        .then((res) => res.json())
        .then((data) => {
          data = data.sleep_record.slice(-parseInt(queryObject.past) - 2, -2);
          data = JSON.stringify(data);
          console.log(queryObject, parseInt(queryObject.past));
          res.end(data);
        });
    } else {
      fetch(file)
        .then((res) => res.json())
        .then((data) => res.end(JSON.stringify(data)));
    }

    // fs.readFile(file, (err, content) => {
    //   if (err) {
    //     if (err.code == "ENOENT") {
    //       res.writeHead(404);
    //       res.end(err.code);
    //     } else {
    //       res.writeHead(500);
    //       res.end(err.code);
    //     }
    //   } else {
    // res.writeHead(200, {
    //   "Content-Type": "application/json",
    //   "Access-Control-Allow-Origin": "*",
    //   "X-Powered-By": "nodejs",
    // });
    //     if ("past" in queryObject) {
    //       data = past_record(parseInt(queryObject.past));
    //       console.log(parseInt(queryObject.past));
    //       res.end(data);
    //     }
    //   }
    // });
  })
  .listen(PORT);
