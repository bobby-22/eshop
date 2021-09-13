<template>
    <footer>
        <div class="footer-content">
            <div class="content">
                <p>
                    Have any improvements or found a bug? Let me know at one of
                    these places &#128578;
                </p>
                <a href="mailto:nlongn22@icloud.com">
                    <i class="fas fa-at"></i>
                </a>
                <a href="https://www.reddit.com/message/compose/?to=bobby--22">
                    <i class="fab fa-reddit"></i>
                </a>
                <a href="https://github.com/bobby-22/marketplace/issues/new">
                    <i class="fab fa-github"></i>
                </a>
            </div>
        </div>
        <div class="footer-bottom">
            <router-link class="terms" to="/terms">Terms and Conditions</router-link>
            <span>&copy; 2021 mechmarket.eu</span>
        </div>
    </footer>
</template>

<script>
export default {
    name: "Footer",
};
</script>

<style scoped>
footer {
    font-weight: 100;
    color: #949494;
    border-top: 1px solid #ededed;
    padding: 15px 30px 15px 30px;
    text-align: center;
}
.footer-content {
    display: flex;
    justify-content: center;
    flex-direction: column;
    border-bottom: 1px solid #f5f5f5;
    margin-bottom: 15px;
    padding-bottom: 15px;
}
p {
    margin: 0px 0px 0px;
}
i {
    font-size: 25px;
}
.fab.fa-reddit {
    margin-left: 10px;
    margin-right: 10px;
}
.footer-bottom {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.terms,
a:link,
a:visited,
a:active,
a:hover {
    color: inherit
}
</style>
