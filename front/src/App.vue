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
                "refresh",
                "copy",
                "move",
                "mkdir",
                "rm_dir",
                "touch",
                "rm_file",
                "download",
                "upload",
                "info",
                "rm_rf",
            ],
        };
    },
};
</script>
<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
        <div>
            <icon
                v-for="icon in topIcons"
                :type="icon"
                :key="icon"
                width="2rem"
            ></icon>
        </div>
        <div>{{ dir }}</div>
        <f-s-table
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
