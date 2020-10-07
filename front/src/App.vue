<script>
import apiCalls from "./requests/index.js";
import Icon from "./components/Icon.vue";
import FSTable from "./components/FSTable.vue";
import InputModal from "./components/InputModal.vue";
import DirModal from "./components/DirModal.vue";
export default {
    name: "App",
    components: {
        Icon,
        FSTable,
        InputModal,
        DirModal,
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
                // "info", // related to any selected
                "rm_rf", // requires confirmation
            ],
            fileOnly: ["copy", "move", "rm_file", "download"],
            dirOnly: ["rm_dir"],
            files: [],

            input: {
                name: "",
                dir: "",
                need_name: false,
                need_dir: false,
                callback: null,
                args: 0, // 1- file, 2-dir 3-both
                need_file: false,
            },
        };
    },
    created() {
        this.setFiles(apiCalls.getFiles, []);
    },
    methods: {
        async setFiles(funct, args) {
            await funct(...args).then((response) => {
                this.files = response.data;
            });
        },
        activeIsDir() {
            return this.active.data;
        },
        callIcon(type) {
            if (this.iconIsNotActive(type)) {
                return;
            }
            let index = this.topIcons.indexOf(type);
            switch (index) {
                case 0:
                    // "refresh"
                    this.setFiles(apiCalls.getFiles, []);
                    break;
                case 1:
                    // copy
                    this.input.need_name = true;
                    this.input.need_dir = true;
                    this.input.callback = apiCalls.copyFile;
                    this.input.args = 3;
                    break;
                case 2:
                    // move
                    // this.input.need_name = true;
                    this.input.need_dir = true;
                    this.input.callback = apiCalls.moveFile;
                    this.input.args = 2;
                    break;
                case 3:
                    // mkdir
                    this.input.need_name = true;
                    this.input.callback = apiCalls.mkdir;
                    this.input.args = 1;
                    break;
                case 4:
                    // rmdir - requires confirmation
                    const r = confirm(
                        `Are you sure, that you want to delete directory ${this.dir}?`
                    );
                    if (r == true) {
                        this.setFiles(apiCalls.rmdir, [this.dir]);
                    }
                    break;
                case 5:
                    // create file
                    this.input.need_name = true;
                    this.input.callback = apiCalls.touch;
                    this.input.args = 1;
                    break;
                case 6:
                    // rm file
                    const conf = confirm(
                        `Are you sure, that you want to delete file ${this.dir}?`
                    );
                    if (conf == true) {
                        this.setFiles(apiCalls.rm_file, [this.dir]);
                    }
                    break;
                case 7:
                    // download
                    this.download();
                    break;
                case 8:
                    // upload
                    this.input.need_file = true;
                    break;
                case 9:
                    // rm rf - requires confirmation
                    const rm = confirm(
                        `Are you sure, that you want to delete everything ${this.dir}?`
                    );
                    if (rm == true) {
                        this.setFiles(apiCalls.rm_rf, []);
                    }
                    this.dir = ".";
                    this.active = {};
                    this.input = {
                        name: "",
                        dir: "",
                        need_name: false,
                        need_dir: false,
                        callback: null,
                        args: 0, // 1- file, 2-dir 3-both
                        need_file: false,
                    };
            }
        },
        iconIsNotActive(type) {
            const f = this.fileOnly.includes(type);
            const d = this.dirOnly.includes(type);
            return !(
                (f && !this.activeIsDir()) ||
                (d && this.activeIsDir()) ||
                (!d && !f) ||
                !this.active.name
            );
        },
        checkExistance(dir, fs = this.files) {
            for (let f of fs) {
                if (f.name == dir[0]) {
                    if (f.data && dir.length > 1) {
                        // if dir -> go deep
                        return this.checkExistance(dir.slice(1), f.data);
                    } else {
                        // if file - return
                        console.log("TRUE");
                        return true;
                    }
                }
            }
            return false;
        },
        checkInput(change) {
            if (change == "name" && this.input.args == 1) {
                // set name - call calback
                let arg = this.input.name;
                // path expreaction
                let dir = this.dir.split("/");
                if (!this.active || !this.active.data) {
                    dir[dir.length - 1] = arg;
                } else {
                    dir.push(arg);
                }
                // check that such file or dir doesn't exist
                if (!this.checkExistance(dir.slice(1))) {
                    dir = dir.join("/");
                    this.setFiles(this.input.callback, [dir]);
                } else {
                    alert(
                        "Such file or directory already exist, please, pick another name"
                    );
                }
                return;
            } else if (change == "dir" && this.input.args == 2) {
                // set dir callback (e.g. move)
                let arg = this.input.dir;
                this.setFiles(this.input.callback, [
                    this.dir,
                    `${arg}/${this.active.name}`,
                ]);
                return;
            } else if (
                this.input.args == 3 &&
                !this.input.need_name &&
                !this.input.need_dir
            ) {
                // set dir+name callback
                let arg = `${this.input.dir}/${this.input.name}`;
                this.setFiles(this.input.callback, [this.dir, arg]);
                return;
            }
        },
        getName(name) {
            this.input.name = name;
            this.input.need_name = false;
            this.checkInput("name");
        },
        getDir(dir) {
            this.input.dir = dir;
            this.input.need_dir = false;
            this.checkInput("dir");
        },
        async download() {
            await apiCalls
                .download(this.dir)
                .then((response) => {
                    const url = window.URL.createObjectURL(
                        new Blob([response.data])
                    );
                    const link = document.createElement("a");
                    link.href = url;
                    link.setAttribute("download", this.active.name); // TODO: change name
                    link.setAttribute("class", "hidden");
                    document.body.appendChild(link);
                    link.click();
                })
                .catch((err) => console.log("Error", err));
        },
        upload(event) {
            const f = event.target.files[0];
            let d = this.dir;
            if (this.active.data) {
                d += "/kostil.txt";
            }
            this.setFiles(apiCalls.upload, [f, d]);
            this.input.need_file = false;
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
        <input v-if="input.need_file" type="file" @change="upload($event)" />
        <input-modal
            v-if="input.need_name"
            @readen="getName($event)"
        ></input-modal>
        <dir-modal
            v-if="input.need_dir"
            @readen="getDir($event)"
            :files="files"
        ></dir-modal>
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
    width: 60%;
    margin: auto;
}
table {
    width: 100%;
}
.hidden {
    opacity: 100%;
    display: none;
}
</style>
