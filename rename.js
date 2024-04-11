import fs from "fs";
import path from "path";
import { naturalCompare, splitext } from "./const.js";

const filepath = "F:\\RIZAL\\TAMBAHAN TEGAL\\NOV\\0DTT\\BALAPULANG +1";
const folders = fs.readdirSync(path.join(filepath)).sort(naturalCompare);

folders.forEach((folder) => {
  // const kota = folder.split("-")[0];
  // const kec = folder.split("-")[1];
  // const desa = folder.split("-")[2];
  const kec = folder.split("~")[0];
  const desa = folder.split("~")[1].replace("+1", "");
  // const newName = `KAB. KENDAL-BOJA-${folder}`;
  // const newName = `KAB. SEMARANG-BANCAK-${desa}`;
  const newName = `KAB. TEGAL-${kec}-${desa}`;

  fs.renameSync(path.join(filepath, folder), path.join(filepath, newName));

  // const files = fs
  //   .readdirSync(path.join(filepath, newName))
  //   .sort(naturalCompare);

  // if (files.length !== 0) {
  //   files.forEach((file) => {
  //     const [filename, ext] = splitext(file);
  //     // console.log(ext);
  //     fs.renameSync(
  //       path.join(filepath, newName, file),
  //       path.join(filepath, newName, `0${ext}`)
  //     );
  //     // if (filename.includes("SPTJM")) {
  //     //   console.log(folder, file);
  //     //   fs.renameSync(
  //     //     path.join(filepath, folder, file),
  //     //     path.join(filepath, folder, `SPTJM${ext}`)
  //     //   );
  //     // }
  //   });
  // }
});
