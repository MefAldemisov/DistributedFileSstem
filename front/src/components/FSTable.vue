<script>
import Icon from "./Icon.vue";
export default {
    name: "FSTable",
    components: {
        Icon,
    },
    props: {
        files: {
            required: true,
        },
    },
    data() {
        return {
            current_location: [],
            active: 0,
            input_value: "",
            need_input: false,
        };
    },
    computed: {
        current_files() {
            let res = this.files;
            for (let i = 0; i < this.current_location.length; i++) {
                res = res[this.current_location[i]].data;
            }

            return res;
        },
        current_path() {
            let str = ".";
            let res = this.files;
            for (let i = 0; i < this.current_location.length; i++) {
                const loc = res[this.current_location[i]];
                res = loc.data;
                str += `/${loc.name}`;
            }
            str += `/${this.current_files[this.active].name}`;

            return str;
        },
    },
    methods: {
        setActive(index) {
            if (this.active != index) {
                this.active = index;
                this.$emit("upd_active", this.current_files[index]);
            } else if (this.current_files[index].data) {
                // if is dir -> go deep
                if (this.current_files[index].data.length > 0) {
                    this.current_location.push(index);
                    this.active = 0;
                } else {
                    alert("The directory is empty");
                }
            }
            this.$emit("upd_dir", this.current_path);
        },
        backDir() {
            this.current_location.pop();
            this.$emit("upd_dir", this.current_path);
            this.$emit("upd_active", this.current_files[0]);
        },
    },
};
</script>
<template>
    <div class="table">
        <table>
            <thead>
                <th>Filename</th>
                <th>Size</th>
                <th>Last update</th>
            </thead>
            <tbody>
                <tr v-if="current_location.length" @click="backDir()">
                    <td><icon type="arrow-back" width="1rem"></icon></td>
                </tr>
                <tr
                    :class="{
                        'active-row': active == file.index,
                        dir: file.data,
                    }"
                    v-for="file in current_files"
                    :key="file.index"
                    @click="setActive(file.index)"
                >
                    <td>
                        <icon v-if="file.data" type="arrow" width="1rem"></icon
                        >{{ file.name }}
                    </td>
                    <td>{{ file.size }}</td>
                    <td>{{ file.upd }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<style>
tr:hover {
    background-color: bisque;
}
.active-row {
    font-weight: 800;
    background-color: bisque;
}
.dir {
    color: darkcyan;
}
</style>