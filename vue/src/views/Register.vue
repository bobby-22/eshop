<template>
<div class="container">
    <div class="field">
        <span class="label">Username</span>
        <div class="control has-icons-left">
            <input class="input is-success" type="text" placeholder="example">
            <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
            </span>
        </div>
        <p class="help is-success">This username is already taken</p>
    </div>

    <div class="field">
        <span class="label">Email</span>
        <div class="control has-icons-left">
            <input class="input is-success" type="text" placeholder="example@example.com">
            <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
            </span>
        </div>
        <p class="help is-danger">This email is already used</p>
    </div>

    <div class="field">
        <span class="label">Password</span>
        <div class="control has-icons-left">
            <input class="input" type="text" placeholder="supersecretpassword">
            <span class="icon is-small is-left">
                <i class="fas fa-key"></i>
            </span>
        </div>
    </div>

    <div class="field">
        <span class="label">Confirm password</span>
        <div class="control has-icons-left">
            <input class="input" type="text" placeholder="supersecretpassword">
            <span class="icon is-small is-left">
                <i class="fas fa-key"></i>
            </span>
        </div>
    </div>

    <div class="field">
        <div class="control">
            <span class="checkbox">
                <input type="checkbox">
                I agree to the <a href="#">terms and conditions</a>
            </span>
        </div>
    </div>

    <div class="field is-grouped">
        <div class="control">
            <button class="button is-link">Submit</button>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "ModalRegister",
    props: {
      modalBoolean: false
    },
    methods: {
      closeModal() {
        this.$emit("modalBooleanChange")
      }
    }
};
</script>

<style lang="scss" scoped>
$modal-content-background-color: white;
.container {
    padding: 30px;
}
.label {
  text-align: start;
}
.checkbox {
  color: black;
}
</style>
