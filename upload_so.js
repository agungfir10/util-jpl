import fs from "fs";
import path from "path";
import FormData from "form-data";
import https from "https";
import url from "url";
import soupload from "./SO.json" assert { type: "json" };

const __dirname = url.fileURLToPath(new URL(".", import.meta.url));
let index = 0;

function uploadSo() {
  const { filename, so, tanggal } = soupload[index];
  const parts = tanggal.split("-");

  const tanggalFormated = `${parts[2]}-${parts[1]}-${parts[0]}`;

  const form = new FormData();

  form.append(
    "file",
    fs.createReadStream(path.join(__dirname, "pdf", "so", `${filename}.pdf`))
  );

  form.append("userid", "GD11040103");
  form.append("tanggal", tanggalFormated);
  form.append("nodoc", so);
  form.append("jenis", "8 | SO-BULOG");
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
      console.log(filename);
      let response = "";
      res.on("data", (chunk) => {
        response += chunk.toString();
      });

      res.on("end", () => {
        console.log(response);
        if (response === "1") {
          console.log("SUKSES");
          index++;
          uploadSo();
        } else if (response.includes("|")) {
          index++;
          uploadSo();
          console.log(so);
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
