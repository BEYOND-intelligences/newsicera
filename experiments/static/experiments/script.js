// بيانات المعرض (Slider Data)
const slidesData = [
    {
        title: "اكتشف قوانين الفيزياء",
        image: "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80",
        actionText: "ابدأ المحاكاة الآن"
    },
    {
        title: "محاكاة النظام الشمسي",
        image: "https://images.unsplash.com/photo-1614728853913-1e22ba7e8d78?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80",
        actionText: "استكشف الفضاء"
    },
    {
        title: "التفاعلات الكيميائية",
        image: "https://images.unsplash.com/photo-1532094349884-543bc11b234d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80",
        actionText: "ادخل المختبر"
    }
];


// وظيفة وهمية عند الضغط على زر التشغيل
function startExperiment(title) {
    alert(`جاري تحميل محاكاة: ${title}...\n(سيتم توجيهك للصفحة الخاصة بالتجربة لاحقاً)`);
    // هنا يمكنك إضافة كود التوجيه الحقيقي: window.location.href = 'simulation.html';
}

// تشغيل الدوال عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', () => {
    initSlider();
    // loadExperiments(); // Removed as experiments are now loaded from backend
});
