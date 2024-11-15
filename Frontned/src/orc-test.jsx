/* import React, { useEffect, useState } from 'react';
import Tesseract from 'tesseract.js';
import image from  "./assets/images.png"

function Data() {
    const [data, setData] = useState('');

    useEffect(() => {
        Tesseract.recognize(image,
            'eng',
            { logger: e => console.log(e) }
        )
        .then(out => {
            setData(out.data.text);
            console.log(out.data.text); // Logs the extracted text in the console
        })
        .catch(error => console.error("Error extracting text:", error));
    }, []);

    return (
        <div>
            <h3>Extracted Text:</h3>
            <p>{data}</p>
        </div>
    );
}

export default Data;
 */

