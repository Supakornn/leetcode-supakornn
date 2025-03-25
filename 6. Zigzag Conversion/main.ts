function convert(s: string, numRows: number): string {
    if (numRows === 1 ) return s
    
    const rows = Array.from({length: Math.min(numRows, s.length)}).map(() => "")
    let down = false
    let row = 0

    for (let i = 0; i < s.length; i++) {
        rows[row] += s[i]
        if (row === 0 || row === numRows - 1) { 
            down = !down
        }
        row += down ? 1 : -1 
    }

    return rows.join("")
};

console.log(convert("PAYPALISHIRING", 3)); // "PAHNAPLSIIGYIR"
