import { useState } from "react";
import { uploadFile } from "../../services/api";

const UploadForm = () => {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Select a file first!");
    await uploadFile(file);
    alert("File uploaded successfully!");
  };

  return (
    <div className="p-4 border rounded-lg bg-white shadow-md">
      <input type="file" className="border p-2 rounded" onChange={(e) => setFile(e.target.files[0])} />
      <button className="ml-2 px-4 py-2 bg-blue-500 text-white rounded" onClick={handleUpload}>
        Upload
      </button>
    </div>
  );
};

export default UploadForm;