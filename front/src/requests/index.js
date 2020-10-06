import axios from "axios";

axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
let apiClient = axios.create({
	baseURL: "http://0.0.0.0:5001",
});
export default {
	getFiles() {
		return apiClient.get("/refresh");
	},
	copyFile(source, destination) {
		return apiClient.get(`/copy?from=${source}&to=${destination}`);
	},
	moveFile(source, destination) {
		return apiClient.get(`/move?from=${source}&to=${destination}`);
	},
	mkdir(path) {
		return apiClient.get(`/mkdir?path=${path}`);
	},
	rmdir(path) {
		return apiClient.get(`/rmdir?path=${path}`);
	},
	touch(path) {
		return apiClient.get(`/touch?path=${path}`);
	},
	rm_file(path) {
		return apiClient.get(`/rm_file?path=${path}`);
	},
	rm_rf() {
		return apiClient.get(`/clear_all`);
	},
	async download(path) {
		// get url to download
		let url;
		await apiClient.get(`/download?path=${path}`).then((response) => {
			url = response.data.url;
		});
		// file promive
		return axios.get(url, {
			responseType: "blob",
		});
	},
	upload(data) {
		let fd = new FormData();
		fd.append("name", data.name);
		fd.append("file", data);

		return apiClient.post(`/upload/`, fd, {
			headers: {
				"Content-Type": "multipart/form-data",
			},
		});
	},
};
