import fs from "fs";
import path from "path";
import FormData from "form-data";
import https from "https";
import url from "url";
import soupload from "./POD.json" assert { type: "json" };

const __dirname = url.fileURLToPath(new URL(".", import.meta.url));
let index = 0;
let indexFile = 0;
const files = fs.readdirSync(path.join(__dirname, "images", "pod"));

function uploadSo() {
  console.log(index, "/", soupload.length);
  if (indexFile === files.length) {
    indexFile = 0;
  }

  const { BAST, TANGGAL } = soupload[index];
  const parts = TANGGAL.split("/");

  const tanggalFormated = `${parts[2]}-${parts[1]}-${parts[0]}`;

  const form = new FormData();

  form.append(
    "file",
    fs.createReadStream(path.join(__dirname, "images", "pod", files[indexFile]))
  );

  form.append("userid", "GD11040103");
  form.append("tanggal", tanggalFormated);
  form.append("nodoc", BAST);
  form.append("jenis", "4 | FOTO PENYERAHAN DROP POINT (input no.BAST)");
  form.append("kdkantor", "11001");

  const headers = form.getHeaders();

  const req = https.request(
    {
      hostname: "astridjplb.id",
      path: "/w/proc/proses_simpan_dokumen.php",
      method: "POST",
      headers: headers,
    },
    (res) => {
      let response = "";
      res.on("data", (chunk) => {
        response += chunk.toString();
      });

      res.on("end", () => {
        console.log(response);
        if (response === "1") {
          console.log("SUKSES");
          index++;
          indexFile++;
          uploadSo();
        } else if (response.includes("|")) {
          index++;
          uploadSo();
          console.log("DOKUMEN SUDAH DI UPLOAD");
        } else {
          uploadSo();
          console.log("GAGAL");
        }
      });
    }
  );
  req.on("error", (error) => {
    console.log(error);
  });

  form.pipe(req);
}

uploadSo();
