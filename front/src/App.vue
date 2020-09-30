<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
        <div>
            <icon type="refresh" width="2rem"></icon>
            <icon type="copy" width="2rem"></icon>
            <icon type="move" width="2rem"></icon>
            <icon type="mkdir" width="2rem"></icon>
            <icon type="rm_dir" width="2rem"></icon>
            <icon type="touch" width="2rem"></icon>
            <icon type="rm_file" width="2rem"></icon>
            <icon type="download" width="2rem"></icon>
            <icon type="upload" width="2rem"></icon>
            <icon type="info" width="2rem"></icon>
            <icon type="rm_rf" width="2rem"></icon>
        </div>
        <table>
            <thead>
                <th>Filename</th>
                <th>Size</th>
                <th>Last update</th>
            </thead>
            <tbody>
                <tr
                    :class="{ active: file.index == active }"
                    v-for="file in files"
                    :key="file.index"
                    @click="setActive(file.index)"
                >
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
                {
                    index: 3,
                    name: "./dist",
                    size: "184",
                    upd: "23.05.20",
                    data: [],
                },
                {
                    index: -1,
                    name: "dir",
                    size: "1024",
                    data: [
                        {
                            index: 0,
                            name: "helloworld.c",
                            size: "256",
                            upd: "23.05.19",
                        },
                        {
                            index: 1,
                            name: "helloworld.cpp",
                            size: "184",
                            upd: "23.05.20",
                        },
                    ],
                },
                {
                    index: 0,
                    name: "helloworld.c",
                    size: "256",
                    upd: "23.05.19",
                },
                {
                    index: 1,
                    name: "helloworld.cpp",
                    size: "184",
                    upd: "23.05.20",
                },
                {
                    index: 2,
                    name: "aaa.txt",
                    size: "256",
                    upd: "23.05.19",
                },
            ],
            active: 0,
        };
    },
    methods: {
        setActive(index) {
            this.active = index;
        },
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
.active {
    font-weight: 800;
    background-color: bisque;
}
</style>
