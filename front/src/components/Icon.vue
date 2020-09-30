<script>
import IconCopy from "./icons/IconCopy.vue";
import IconDownload from "./icons/IconDownload.vue";
import IconInfo from "./icons/IconInfo.vue";
import IconMkDir from "./icons/IconMkDir.vue";
import IconMove from "./icons/IconMove.vue";
import IconRefresh from "./icons/IconRefresh.vue";
import IconRmDir from "./icons/IconRmDir.vue";
import IconRmFile from "./icons/IconRmFile.vue";
import IconRmRf from "./icons/IconRmRf.vue";
import IconTouch from "./icons/IconTouch.vue";
import IconUpload from "./icons/IconUpload.vue";

export default {
    name: "Icon",
    props: {
        type: {
            default: "info",
        },
        width: {
            default: "1.5rem",
        },
    },
    components: {
        IconCopy,
        IconDownload,
        IconInfo,
        IconMkDir,
        IconMove,
        IconRefresh,
        IconRmDir,
        IconRmFile,
        IconRmRf,
        IconTouch,
        IconUpload,
    },
};
</script>
<template>
    <div class="inline hoverable" :title="type">
        <icon-copy :width="width" v-if="type == 'copy'"></icon-copy>
        <icon-download :width="width" v-if="type == 'download'"></icon-download>
        <icon-info :width="width" v-if="type == 'info'"></icon-info>
        <icon-mk-dir :width="width" v-if="type == 'mkdir'"></icon-mk-dir>
        <icon-move :width="width" v-if="type == 'move'"></icon-move>
        <icon-refresh :width="width" v-if="type == 'refresh'"></icon-refresh>
        <icon-rm-dir :width="width" v-if="type == 'rm_dir'"></icon-rm-dir>
        <icon-rm-file :width="width" v-if="type == 'rm_file'"></icon-rm-file>
        <icon-rm-rf :width="width" v-if="type == 'rm_rf'"></icon-rm-rf>
        <icon-touch :width="width" v-if="type == 'touch'"></icon-touch>
        <icon-upload :width="width" v-if="type == 'upload'"></icon-upload>
    </div>
</template>
<style scoped>
.inline {
    display: inline-block;
    margin: 10px;
}
.hoverable:hover {
    transform: scale(1.5);
}
</style>

