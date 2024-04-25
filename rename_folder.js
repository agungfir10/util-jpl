import { renameSync, readdirSync } from "fs";
import { join } from "path";
import { naturalCompare, splitext } from "./const.js";

const path = "F:\\+3\\PANGKAH~SEPT";
const folders = readdirSync(join(path)).sort(naturalCompare);

folders.forEach((folder) => {
//   const kota = folder.split("-")[0];
  // const kec = folder.split("-")[1];
  // const desa = folder.split("-")[2];
//   // const kec = folder.split("~")[0];
//   // const desa = folder.split("~")[1].replace("+1", "");
  const newName = `KAB. TEGAL-PANGKAH-${folder}`;
  // const newName = `KAB. GROBOGAN-TANGGUNGHARJO-${desa}`;
// const newName = `KAB. DEMAK-${kec}-${desa}`;

renameSync(join(path, folder), join(path, newName));

//   // const files = fs
//   //   .readdirSync(join(path, newName))
//   //   .sort(naturalCompare);

//   // if (files.length !== 0) {
//   //   files.forEach((file) => {
//   //     const [filename, ext] = splitext(file);
//   //     // console.log(ext);
//   //     renameSync(
//   //       join(path, newName, file),
//   //       join(path, newName, `0${ext}`)
//   //     );
//   //     // if (filename.includes("SPTJM")) {
//   //     //   console.log(folder, file);
//   //     //   renameSync(
//   //     //     join(path, folder, file),
//   //     //     join(path, folder, `SPTJM${ext}`)
//   //     //   );
//   //     // }
//   //   });
//   // }
});

// folders.forEach((folder) => {
//   const subFolders = readdirSync(join(path, folder));
//   subFolders.forEach((subfolder) => {
//     // const kec = subfolder.split("-")[1];
//     // const desa = subfolder.split("-")[2];
//     const newName = `KOTA PEKALONGAN-${folder}-${subfolder}`;
//     renameSync(join(path, folder, subfolder), join(path, folder, newName));
//   });
// });
// folders.forEach((folder) => {
//   const newName = folder.replaceAll("NOV ", "");
//   renameSync(join(path, folder), join(path, newName));
// });
