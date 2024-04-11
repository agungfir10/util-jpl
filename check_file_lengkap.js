import { readdirSync, accessSync, renameSync } from "fs";
import { join } from "path";
import { naturalCompare } from "./const.js";

const path =
  "D:\\EKS KARESIDENAN SEMARANG\\4 DESEMBER\\DESEMBER\\KAB KENDAL\\ALL\\BELUM ADA DTT\\New folder";

const folders = readdirSync(path).sort(naturalCompare);

folders.forEach((folder, index) => {
  // const kota = folder.split("-")[0];
  // const kec = folder.split("-")[1];
  // const desa = folder.split("-")[2];

  const files = readdirSync(path, folder).sort(naturalCompare);

  files.forEach((file, i) => {
    console.log(file);
    if (file.includes("DO") && file.includes(".pdf")) {
      try {
        // accessSync(join(path, folder, `${desa}.pdf`));
        renameSync(
          join(path, folder, file),
          join(path, folder, `${index}-${i}.pdf`)
        );
      } catch (e) {
        console.log(folder);
      }
    }
  });
});
