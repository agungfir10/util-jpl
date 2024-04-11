import { exec } from "child_process";
import fs from "fs";
import path from "path";
import { __dirname } from "./const.js";

let index = 0;
const files = fs.readdirSync("result/so");
let so = [];
function tesseract() {
  console.log(files[index]);
  let filenameImage = files[index].includes(" ")
    ? `"./result/so/${files[index]}"`
    : `./result/so/${files[index]}`;

  exec(`tesseract ${filenameImage} stdout -l ind+eng`, (error, stdout) => {
    if (error) {
      tesseract();
    } else {
      let formatSO = "";
      const out = stdout;
      if (out.includes("S0/")) {
        const indexSO = out.indexOf("S0/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("S0/", "SO/");
      } else if (out.includes("$0/")) {
        const indexSO = out.indexOf("$0/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("$0/", "SO/");
      } else if (out.includes("50/")) {
        const indexSO = out.indexOf("50/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("50/", "SO/");
      } else if (out.includes("§0/")) {
        const indexSO = out.indexOf("§0/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("§0/", "SO/");
      } else if (out.includes("$Q/")) {
        const indexSO = out.indexOf("$Q/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("$Q/", "SO/");
      } else if (out.includes("S9/")) {
        const indexSO = out.indexOf("S9/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("S9/", "SO/");
      } else if (out.includes("SO/")) {
        const indexSO = out.indexOf("SO/");
        formatSO = out.slice(indexSO + 3, indexSO + 8).replace("SO/", "SO/");
      } else {
        console.log(stdout);
      }

      console.log(files[index], formatSO);
      let tanggal = "";
      if (stdout.includes("09-2023")) {
        const indexTanggal = stdout.indexOf("09-2023");
        tanggal = stdout.slice(indexTanggal - 3, indexTanggal - 3 + 10);
        console.log(tanggal);
      }

      if (stdout.includes("10-2023")) {
        const indexTanggal = stdout.indexOf("10-2023");
        tanggal = stdout.slice(indexTanggal - 3, indexTanggal - 3 + 10);
        console.log(tanggal);
      }

      if (stdout.includes("11-2023")) {
        const indexTanggal = stdout.indexOf("11-2023");
        tanggal = stdout.slice(indexTanggal - 3, indexTanggal - 3 + 10);
        console.log(tanggal);
      }

      if (stdout.includes("12-2023")) {
        const indexTanggal = stdout.indexOf("12-2023");
        tanggal = stdout.slice(indexTanggal - 3, indexTanggal - 3 + 10);
        console.log(tanggal);
      }

      fs.appendFileSync(
        path.join(__dirname, "SO.txt"),
        `${formatSO} ${tanggal} ${filenameImage}\n`
      );

      so.push({ tanggal, so: formatSO, filename: files[index] });
      if (index <= files.length) {
        index++;
        tesseract();
      }

      fs.writeFileSync(path.join(__dirname, "SO.json"), JSON.stringify(so));
    }
  });
}

tesseract();
