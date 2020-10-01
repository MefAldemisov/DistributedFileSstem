<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);
Vue.config.productionTip = false;

import Icon from "./components/Icon.vue";
import FSTable from "./components/FSTable.vue";
export default {
    name: "App",
    components: {
        Icon,
        FSTable,
    },
    data() {
        return {
            dir: ".",
            active: {},
            topIcons: [
                "refresh", // not related to selected
                "copy", // applicable ONLY to file
                "move", // applicable ONLY to file
                "mkdir", // not related to selected
                "rm_dir", // applicable only to DIR, requires confirmation
                "touch", // not related to delected
                "rm_file", // applicable ONLY to file
                "download", // applicable ONLY to file
                "upload", // not related to selcted
                "info", // related to any selected
                "rm_rf", // requires confirmation
            ],
            fileOnly: ["copy", "move", "rm_file", "download"],
            dirOnly: ["rm_dir"],
            files: [],
        };
    },
    created() {
        this.getFiles();
        this.copyFile("./helloworld.c", "./dist/helloworld1.c");
        this.moveFile("./helloworld.c", "./dist/helloworld1.c");
    },
    methods: {
        getFiles() {
            axios
                .get("http://0.0.0.0:5000/refresh")
                .then((response) => {
                    this.files = response.data[0];
                    console.log(this.files.length);
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        copyFile(source, destination) {
            axios
                .get(
                    `http://0.0.0.0:5000/copy?from=${source}&to=${destination}`
                )
                .then((response) => {
                    this.files = response.data[0];
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        moveFile(source, destination) {
            axios
                .get(
                    `http://0.0.0.0:5000/move?from=${source}&to=${destination}`
                )
                .then((response) => {
                    this.files = response.data[0];
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        activeIsDir() {
            return this.active.data;
        },
        callIcon(type) {
            if (this.iconIsNotActive(type)) {
                return;
            }
            alert(type);
        },
        iconIsNotActive(type) {
            const f = this.fileOnly.includes(type);
            const d = this.dirOnly.includes(type);
            return !(
                (f && !this.activeIsDir()) ||
                (d && this.activeIsDir()) ||
                (!d && !f && this.active.name)
            );
        },
    },
};
</script>
<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
        <div>
            <span v-for="type in topIcons" @click="callIcon(type)" :key="type">
                <icon
                    :type="type"
                    width="2rem"
                    :disabled="iconIsNotActive(type)"
                ></icon>
            </span>
        </div>
        <div>{{ dir }}</div>
        <f-s-table
            :files="files"
            @upd_active="active = $event"
            @upd_dir="dir = $event"
        ></f-s-table>
    </div>
</template>
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
</style>
