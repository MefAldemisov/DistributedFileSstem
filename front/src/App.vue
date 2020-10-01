<script>
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
            files: [
                {
                    index: 0,
                    name: "dist",
                    size: "0",
                    upd: "23.05.20",
                    data: [],
                },
                {
                    index: 1,
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
                    index: 2,
                    name: "helloworld.c",
                    size: "256",
                    upd: "23.05.19",
                },
                {
                    index: 3,
                    name: "helloworld.cpp",
                    size: "184",
                    upd: "23.05.20",
                },
                {
                    index: 4,
                    name: "aaa.txt",
                    size: "256",
                    upd: "23.05.19",
                },
            ],
        };
    },
    methods: {
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
