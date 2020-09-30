<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
        <div>
            <icon type="copy" width="2rem"></icon>
            <icon type="download" width="2rem"></icon>
            <icon type="info" width="2rem"></icon>
            <icon type="mkdir" width="2rem"></icon>
            <icon type="move" width="2rem"></icon>
            <icon type="refresh" width="2rem"></icon>
            <icon type="rm_dir" width="2rem"></icon>
            <icon type="rm_file" width="2rem"></icon>
            <icon type="rm_rf" width="2rem"></icon>
            <icon type="touch" width="2rem"></icon>
            <icon type="upload" width="2rem"></icon>
        </div>
        <table>
            <thead>
                <th>Filename</th>
                <th>Size</th>
                <th>Last update</th>
            </thead>
            <tbody>
                <tr v-for="file in files" :key="file.name">
                    <td>{{ file.name }}</td>
                    <td>{{ file.size }}</td>
                    <td>{{ file.upd }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import Icon from "./components/Icon.vue";

export default {
    name: "App",
    components: {
        Icon,
    },
    data() {
        return {
            files: [
                { name: "helloworld.c", size: "256", upd: "23.05.19" },
                { name: "helloworld.cpp", size: "184", upd: "23.05.20" },
            ],
        };
    },
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
table {
    width: 60%;
    margin: auto;
}
tr:hover {
    background-color: bisque;
}
</style>
