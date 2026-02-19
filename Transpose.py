function transpose(mat) {
    const rows = mat.length;           
    const cols = mat[0].length;      

    // Create a result matrix of size
    // cols x rows for the transpose
    const tMat = new Array(cols).fill(0).map(() =>
                                new Array(rows).fill(0));

    // Fill the transposed matrix by
    // swapping rows with columns
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
      
            // Assign transposed value
            tMat[j][i] = mat[i][j];
        }
    }

    return tMat; 
}


// example usage
const mat = [[1, 1, 1, 1],[2, 2, 2, 2],[3, 3, 3, 3], [4, 4, 4, 4]];
const res = transpose(mat);
for (const row of res) {
    console.log(row.join(" "));
}
