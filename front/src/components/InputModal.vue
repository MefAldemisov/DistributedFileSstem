<script>
export default {
    name: "InputModal",
    data() {
        return {
            input_value: "",
        };
    },
    methods: {
        done() {
            this.$emit("readen", this.input_value);
        },
    },
};
</script>
<template>
    <div>
        <div>Enter the new file name:</div>
        <input
            class="modal-input"
            v-model="input_value"
            placeholder="new file"
        />
        <button class="modal-btn" @click="done()">Ok</button>
    </div>
</template>
<style scoped>
.modal-input {
    width: 80%;
    height: 1.5rem;
    text-align: center;
    font-size: 1.1rem;
    border: 1px solid darkcyan;
}
.modal-btn {
    height: 100%;
    text-align: center;
    font-size: 1.1rem;
    border: 1px solid darkcyan;
    padding: 2.5px 1rem;
}
</style>