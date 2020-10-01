import axios from "axios";

axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
let apiClient = axios.create({
	baseURL: "http://0.0.0.0:5000",
});
export default {
	getFiles() {
		return apiClient.get("/refresh");
		// .then((response) => {
		// 	return response.data[0];
		// });
	},
	copyFile(source, destination) {
		return apiClient.get(`/copy?from=${source}&to=${destination}`);

		// .then((response) => {
		// 	return response.data[0];
		// });
	},
	moveFile(source, destination) {
		return apiClient.get(`/move?from=${source}&to=${destination}`);

		// .then((response) => {
		// 	return response.data[0];
		// });
	},
};
