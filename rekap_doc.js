import { exec } from "child_process";
import FormData from "form-data";
import https from "https";
import { JSDOM } from "jsdom";
import xlsx from "json-as-xlsx";
import { join } from "path";
import { REKAP_DOCUMENT, __dirname } from "./const.js";
import { formatDate, getCurrentTime, getKeteranganAlokasi, getKodeAlokasi, getTab } from './src/utils.js'
import cities from "./data/KABUPATEN-KOTA-KECAMATAN.json" assert { type: "json" };
import { argv } from 'process';
import { writeFileSync, readFileSync } from 'fs'
if (argv.length < 3) {
    throw new Error('Argumen tidak lengkap!')
}
let index = 0;
const tahap = getKodeAlokasi(argv[2]);

let rekap = [];
let data = []
let dataUpload = []
let differentCity = false
function getRekap() {
    if (index < cities.length) {
        if (cities[index + 1] !== undefined) {
            if (differentCity) {
                const dataExcelKota = getDataToExcel(rekap, cities[index - 1].KOTA)
                data.push(dataExcelKota);
                dataUpload.push(...rekap)
                rekap = []
                differentCity = false
            }

            if (cities[index].KOTA !== cities[index + 1].KOTA) {
                differentCity = true
                rekapDoc(cities[index])
            } else {
                rekapDoc(cities[index])
            }

        } else {
            rekapDoc(cities[index])
        }
    } else {
        const dataExcelKota = getDataToExcel(rekap, cities[index - 1].KOTA)
        data.push(dataExcelKota);
        dataUpload.push(...rekap)
        rekap = []
        const fileName = "REKAP DOCUMENT " + tahap.split("|")[1].trimStart() + " " + formatDate(new Date()) + " " + getCurrentTime();
        xlsx(data, {
            fileName: join(REKAP_DOCUMENT, fileName),
        });
        const dataReguler = dataUpload.filter(data => data.NO_DTT.includes('23110'))
        saveJsonWithDate(dataReguler, 'REG');

        const dataTambahan1 = dataUpload.filter(data => data.NO_DTT.includes('23114'))
        saveJsonWithDate(dataTambahan1, '+1');
        const dataTambahan2 = dataUpload.filter(data => data.NO_DTT.includes('23115'))
        saveJsonWithDate(dataTambahan2, '+2');
        const dataTambahan3 = dataUpload.filter(data => data.NO_DTT.includes('23116'))
        saveJsonWithDate(dataTambahan3, '+3');

        console.log("Rekap Selesai...");
    }
}

function rekapDoc(city) {
    const { KOTA, KECAMATAN } = city;
    const text = getTab(`${KOTA}-${KECAMATAN}`, 8);
    process.stdout.write(`${KOTA}-${KECAMATAN}`);
    process.stdout.write(text);
    process.stdout.write(`${index + 1}/${cities.length}\n`);

    const form = new FormData();
    form.append("userid", "A110010001");
    form.append("kdkantor", "11001");
    form.append("namakantor", "JPLB-CABANG JATENG");
    form.append("tahap", tahap);
    form.append("propinsi", "JAWA TENGAH");
    form.append("kota", KOTA);
    form.append("kecamatan", KECAMATAN);
    const req = https.request(
        {
            hostname: "astridjplb.id",
            path: "/w/10/report/lap_dokumen_tampil.php",
            method: "POST",
            headers: form.getHeaders(),
        },
        (res) => {
            let html = "";
            res.on("data", (chunk) => {
                html += chunk.toString();
            });
            res.on("end", () => {
                if (html !== "0") {
                    const dom = new JSDOM(html);
                    const elTable = dom.window.document.querySelector(
                        "#data-table-responsive"
                    );
                    const tbodies = elTable.children[1];
                    for (let i = 0; i < tbodies.children.length; i++) {
                        const contents = tbodies.children[i];
                        const NO_DTT = contents.children[3].textContent;
                        const DTT = contents.children[7].textContent;
                        const SPTJM = contents.children[11].textContent;
                        const PENGGANTI = contents.children[12].textContent;
                        const PERWAKILAN = contents.children[13].textContent;
                        const DESA = contents.children[2].textContent.trim();
                        const PERSENTASE = contents.children[15].textContent;


                        rekap.push({
                            KOTA,
                            KECAMATAN,
                            DESA,
                            NO_DTT,
                            DTT,
                            SPTJM,
                            PENGGANTI,
                            PERWAKILAN,
                            PERSENTASE
                        });
                    }
                    index++;
                    getRekap();
                } else {
                    getRekap();
                }
            });
        }
    );
    req.on("error", (error) => {
        console.log(error);
        getRekap();
    });
    form.pipe(req);
}

function saveJsonWithDate(data, ket) {
    const tahap = argv[2]
    const keterangan = getKeteranganAlokasi(ket)
    let newDtt = []
    let cocok = false;


    if (data.length !== 0) {
        const tanggal = JSON.parse(readFileSync(join(__dirname, 'data', `TANGGAL_${tahap}_${keterangan}.json`)))
        data.forEach((d) => {
            for (let i = 0; i < tanggal.length; i++) {
                const t = tanggal[i];

                if (d.KOTA === t.KOTA && d.KECAMATAN === t.KECAMATAN && t.DESA === d.DESA) {
                    newDtt.push({ ...d, TANGGAL: t.TANGGAL });
                    cocok = true;
                    break;
                }
            }

            if (!cocok) {
                newDtt.push({ ...d });
                cocok = false;
            }
        })
        writeFileSync(join(__dirname, 'data', `${tahap}_${keterangan}_UPLOAD.json`), JSON.stringify(newDtt))
    }
}

function getDataToExcel(dataKota, kota) {
    const rekapFilter = Array.from(new Set(dataKota.map((a) => a.NO_DTT))).map(
        (NO_DTT) => {
            return dataKota.find((a) => a.NO_DTT === NO_DTT);
        }
    );
    return {
        sheet: kota,
        columns: [
            { label: "KOTA", value: "KOTA" },
            { label: "KECAMATAN", value: "KECAMATAN" },
            { label: "DESA", value: "DESA" },
            { label: "NO_DTT", value: "NO_DTT" },
            { label: "DTT", value: "DTT" },
            { label: "SPTJM", value: "SPTJM" },
            { label: "PENGGANTI", value: "PENGGANTI" },
            { label: "PERWAKILAN", value: "PERWAKILAN" },
            { label: "PERSENTASE", value: "PERSENTASE" },
        ],
        content: rekapFilter,
    };
}

getRekap();
