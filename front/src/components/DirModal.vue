<script>
export default {
    name: "DirModal",
    props: {
        files: {
            required: true,
        },
    },
    data() {
        return {
            selected: "",
        };
    },
    methods: {
        // list of paths
        listOfPaths(dir, path) {
            // initial input is files
            let paths = [path];
            for (let i = 0; i < dir.length; i++) {
                if (dir[i].data) {
                    // if is dir
                    const subdirs = this.listOfPaths(
                        dir[i].data,
                        path + "/" + dir[i].name
                    );
                    subdirs.forEach((el) => {
                        paths.push(el);
                    });
                }
            }
            return paths;
        },
        setActive(path) {
            this.selected = path;
        },
        done() {
            this.$emit("readen", this.selected);
        },
    },
};
</script>
<template>
    <div>
        <div>
            <span>Select the target directory</span>
            <button class="modal-btn" @click="done()">Ok</button>
        </div>
        <div class="dropout">
            <div
                class="list-item"
                v-for="path in listOfPaths(files, '.')"
                :key="path"
                :class="{ active: selected == path }"
                @click="setActive(path)"
            >
                {{ path }}
            </div>
        </div>
    </div>
</template>
<style scoped>
.list-item:hover {
    background-color: bisque;
}
.active {
    font-weight: 800;
    background-color: bisque;
}
button {
    margin: 0 1rem;
}
</style>