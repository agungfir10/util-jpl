export function getTab(text, width) {
    const count_tab = text.length / 8;
    const add_tab = width - count_tab;
    let string = "";
    for (let i = 0; i < add_tab; i++) {
        string += "\t";
    }
    return string;
}

export function naturalCompare(a, b) {
    const collator = new Intl.Collator(undefined, {
        numeric: true,
        sensitivity: "base",
    });
    return collator.compare(a, b);
}

export function formatDate(date) {
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();

    day = day < 10 ? "0" + day : day;
    month = month < 10 ? "0" + month : month;

    return `${day}-${month}-${year}`;
}

export function getKodeAlokasi(bulan) {
    const bulanUpper = bulan.toUpperCase();
    if (bulanUpper === "SEPTEMBER") {
        return "21 | SEPTEMBER";
    } else if (bulanUpper === "OKTOBER") {
        return "22 | OKTOBER";
    } else if (bulanUpper === "NOVEMBER") {
        return "23 | NOVEMBER";
    } else if (bulanUpper === "DESEMBER") {
        return "31 | DESEMBER";
    } else {
        throw new Error("SALAH ALOKASI");
    }
}

export function getKodeAlokasi(alokasi) {
    if (alokasi === "SEP") {
        return "21 | SEPTEMBER";
    } else if (alokasi === "OKT") {
        return "22 | OKTOBER";
    } else if (alokasi === "NOV") {
        return "23 | NOVEMBER";
    } else if (alokasi === "DES") {
        return "31 | DESEMBER";
    } else {
        throw new Error("Alokasi salah!");
    }
}

export function getCurrentTime() {
    let now = new Date();
    let hour = now.getHours();
    let minute = now.getMinutes();
    return hour + "-" + minute;
}

export function getKeteranganAlokasi(keterangan) {
    if (keterangan === "REG") {
        return "REG";
    } else if (keterangan === "+1") {
        return "TAMBAHAN_1";
    } else if (keterangan === "+2") {
        return "TAMBAHAN_2";
    } else if (keterangan === "+3") {
        return "TAMBAHAN_3";
    } else {
        throw new Error("Keterangan alokasi salah!");
    }
}