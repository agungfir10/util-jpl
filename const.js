import url from "url";
import { readFileSync } from "fs";
import { join } from "path";
export const __dirname = url.fileURLToPath(new URL(".", import.meta.url));

export function naturalCompare(a, b) {
  const collator = new Intl.Collator(undefined, {
    numeric: true,
    sensitivity: "base",
  });
  return collator.compare(a, b);
}

export function containsNumberLoop(str) {
  for (var i = 0; i < str.length; i++) {
    if (!isNaN(parseInt(str[i]))) {
      return true;
    }
  }
  return false;
}

export function formatDate(date) {
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();

  return `${year}-${month}-${day}`;
}

export function splitext(filepath) {
  let index = filepath.lastIndexOf(".");
  if (index === -1) {
    return [filepath, ""];
  } else {
    return [filepath.slice(0, index), filepath.slice(index)];
  }
}

export const SIMPAN_SO = "SIMPAN_SO";
export const TAMPIL_SO = "TAMPIL_SO";
export const TAMPIL_SO_HARI_INI = "TAMPIL_SO_HARI_INI";
export const FILE_SO = "so.json";
export const DIR_DATA = "data";
export const LOGOUT_ADMIN = "LOGOUT_ADMIN";
export const TAMPILKAN_REKAP_DOKUMEN = "REKAP_DOKUMEN";
export const REKAP_DOKUMEN_DESEMBER = "REKAP_DOKUMEN_DESEMBER";
export const REKAP_DOKUMEN_NOVEMBER = "REKAP_DOKUMEN_NOVEMBER";
export const REKAP_DOKUMEN_OKTOBER = "REKAP_DOKUMEN_OKTOBER";
export const REKAP_DOKUMEN_SEPTEMBER = "REKAP_DOKUMEN_SEPTEMBER";
export const DTT_DIR = "C:\\Users\\agung\\Documents\\JPLOGISTICS\\DTT";
export const SPM_DIR = "C:\\Users\\agung\\Documents\\JPLOGISTICS\\SPM";
export const PHOTOS_DIR = "C:\\Users\\agung\\Documents\\FOTO PBP\\PEMALANG";
export const REKAP_DOCUMENT = "/Users/agungfir/Documents/JPLOGISTICS";
export const OPTIONS_MINIFY = {
  continueOnParseError: true,
  minifyCSS: true,
  minifyJS: true,
  quoteCharacter: '"',
  collapseWhitespace: true,
  removeComments: true,
};

export const CSS = readFileSync(join(__dirname, "css", "style.css"), "utf8");
export const STYLE_CSS = `<style>${CSS}</style>`;
export const CACHE_DTT = `${__dirname}\\dtt\\cache`;
export const CACHE_SPM = `${__dirname}\\spm\\cache`;

export const SOURCE_SITE = "http://astridjplb.id/w/";

export const banner = `

 ▄▄▄██▀▀▀██▓███   ██▓     ▒█████    ▄████  ██▓  ██████ ▄▄▄█████▓ ██▓ ▄████▄    ██████ 
   ▒██  ▓██░  ██▒▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▒██    ▒ 
   ░██  ▓██░ ██▓▒▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒██▒▒▓█    ▄ ░ ▓██▄   
▓██▄██▓ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░▓█  ██▓░██░  ▒   ██▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒  ▒   ██▒
 ▓███▒  ▒██▒ ░  ░░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██████▒▒  ▒██▒ ░ ░██░▒ ▓███▀ ░▒██████▒▒
 ▒▓▒▒░  ▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░
 ▒ ░▒░  ░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░▒  ░ ░    ░     ▒ ░  ░  ▒   ░ ░▒  ░ ░
 ░ ░ ░  ░░         ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░░  ░  ░    ░       ▒ ░░        ░  ░  ░  
 ░   ░               ░  ░    ░ ░        ░  ░        ░            ░  ░ ░            ░  

`;


