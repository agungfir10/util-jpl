import chalk from "chalk";
import FormData from "form-data";
import https from "https";
import { argv } from "process";
import { formatDate } from "./const.js";
import { readFileSync } from 'fs'
import { join } from 'path'

const dtt = JSON.parse(
    readFileSync(join(__dirname, "data", `SEP_REG_BATAL_FIX.json`))
);

let index = 0;

function uploadDtt() {
    if (index < dtt.length) {
        const { NO_DTT, KOTA, KECAMATAN, DESA } = dtt[index];
        const folder = `${KOTA}-${KECAMATAN}-${DESA}`;

        if (dtt[index]['SPTJM'] === '') {
            const form = new FormData();
            form.append("userid", "A110010001");
            form.append("datar", `2024-04-26|11001|10|0|${NO_DTT}`);
            form.append("kdkantor", '11001');
            const headers = form.getHeaders();
            const req = https.request(
                {
                    hostname: "astridjplb.id",
                    path: "/w/proc/proses_docout_tolak.php",
                    method: "POST",
                    headers: headers,
                },
                (res) => {
                    let response = "";
                    res.on("data", (chunk) => {
                        response += chunk.toString();
                    });
                    res.on("end", () => {
                        if (response === "9") {
                            const date = formatDate(new Date());
                            console.log(folder);
                            console.log(chalk.white.bgGreen("SUKSES"));
                            index++;
                            uploadDtt();
                        } else {
                            uploadDtt();
                            console.log(response);
                            console.log(chalk.white.bgRed('"GAGAL"'), "CEK UKURAN BERKAS");
                        }
                    });
                }
            );
            req.on("error", (error) => {
                console.log(error);
                uploadDtt();
            });
            form.pipe(req);


        } else {
            index++;
            uploadDtt()
        }
    } else {
        console.log("Selesai...");
    }
}

uploadDtt()