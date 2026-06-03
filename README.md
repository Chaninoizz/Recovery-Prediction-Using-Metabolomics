MetaboRecovery AI

Metabolomics-Based Clinical Decision Support System for Post-Operative Recovery Prediction

ภาพรวมโครงการ

MetaboRecovery AI เป็นระบบ Clinical Decision Support System (CDSS) ที่พัฒนาขึ้นเพื่อวิเคราะห์ข้อมูล Metabolomics จากเลือดผู้ป่วยหลังการผ่าตัด และทำนายแนวโน้มการฟื้นตัวของผู้ป่วยด้วยเทคนิค Machine Learning

ระบบถูกออกแบบภายใต้แนวคิด Explainable AI (XAI) เพื่อให้สามารถอธิบายเหตุผลของการทำนายได้ผ่านการวิเคราะห์ Biomarker ที่มีอิทธิพลต่อผลลัพธ์ของโมเดล

⸻

วัตถุประสงค์

1. ทำนายผลการฟื้นตัวของผู้ป่วยหลังการผ่าตัด
2. ค้นหา Biomarker สำคัญที่เกี่ยวข้องกับกระบวนการฟื้นตัว
3. อธิบายผลการทำนายของ AI อย่างโปร่งใส
4. สนับสนุนการตัดสินใจทางคลินิกของบุคลากรทางการแพทย์

⸻

ข้อมูลที่ใช้

Dataset ที่ใช้พัฒนาระบบมาจากข้อมูล NMR Metabolomics ของผู้ป่วยหลังการผ่าตัด

* จำนวนผู้ป่วย: 47 ราย
* ประเภทข้อมูล: Blood Metabolomics
* รูปแบบข้อมูล: Metabolite Profiles
* Outcome:
    * Fast Recovery
    * Poor Recovery

⸻

วิธีการพัฒนาโมเดล

Data Processing

* Data Cleaning
* Feature Selection
* Feature Engineering
* Standardization

Machine Learning

โมเดลหลักที่เลือกใช้คือ

* Random Forest Classifier

เนื่องจากให้ผลลัพธ์ที่ดีที่สุดสำหรับข้อมูลชุดนี้

Validation

* Stratified 5-Fold Cross Validation

ผลลัพธ์ที่ได้

* Accuracy: 91.56%

⸻

ผลลัพธ์ของระบบ

Recovery Outcome Prediction

ระบบสามารถทำนายแนวโน้มการฟื้นตัวของผู้ป่วยได้เป็น 2 กลุ่ม

* Fast Recovery
* Poor Recovery

พร้อมรายงาน

* Prediction Confidence
* Clinical Risk Level
* AI Risk Score

⸻

Biomarker Discovery

ระบบสามารถค้นหา Biomarker ที่มีอิทธิพลต่อการทำนายได้

ตัวอย่าง Biomarker สำคัญที่ค้นพบ

1. clinical_score
2. glycine_preop
3. L-glutamine_3m
4. L-allo-Isoleucine_3m
5. creatinine_preop
6. L-valine_preop
7. (R)-3-Hydroxybutyric acid_3m

Biomarker เหล่านี้ถูกนำมาใช้ในการสร้าง Clinical Report และการอธิบายผลลัพธ์ของ AI

⸻

Explainable AI

ระบบสามารถอธิบายเหตุผลของการทำนายได้ผ่าน

* Feature Importance Analysis
* Biomarker Deviation Analysis
* Clinical Interpretation
* Risk Assessment

ช่วยให้ผู้ใช้งานสามารถเข้าใจได้ว่าปัจจัยใดส่งผลต่อผลการทำนาย

⸻

Metabolic Pattern Analysis

นอกเหนือจากการทำนายผลการฟื้นตัว ระบบยังสามารถวิเคราะห์รูปแบบทางเมตาบอลิซึม (Metabolic Patterns) ของผู้ป่วยจาก Biomarker ที่ตรวจพบ

ระบบสามารถระบุความคล้ายคลึงกับรูปแบบที่รายงานในงานวิจัยด้านเมตาบอลิซึม เช่น

Strong Association

* Insulin Resistance Pattern
* Metabolic Syndrome Risk

Moderate Association

* Diabetes-like Metabolic Signature
* Hypertension-associated Metabolic Pattern

ผลลัพธ์ส่วนนี้มีวัตถุประสงค์เพื่อสนับสนุนการวิเคราะห์เชิงวิจัยและการตัดสินใจทางคลินิกเท่านั้น

ไม่ใช่การวินิจฉัยโรคโดยตรง

⸻

Clinical Report

ระบบสามารถสร้างรายงานอัตโนมัติสำหรับผู้ป่วยแต่ละราย ประกอบด้วย

* Prediction Result
* Confidence Score
* Key Clinical Drivers
* Metabolic Alerts
* Biomarker Interpretation
* Clinical Risk Summary
* Final Assessment
* Metabolic Pattern Analysis

⸻

Dashboard Prototype

Prototype ถูกออกแบบในรูปแบบ Clinical AI Dashboard เพื่อแสดงข้อมูลสำคัญ เช่น

* Model Performance
* Cohort Information
* Biomarker Importance
* Recovery Distribution
* PCA Clustering
* Clinical Reports
* Explainable AI Analysis

⸻

ข้อจำกัดของระบบ

* Dataset มีขนาดค่อนข้างเล็ก (47 ราย)
* ผลลัพธ์ยังไม่สามารถใช้เป็นการวินิจฉัยทางการแพทย์ได้
* จำเป็นต้องมีการทดสอบเพิ่มเติมกับข้อมูลจากหลายศูนย์วิจัย

⸻

แนวทางพัฒนาในอนาคต

* เพิ่มจำนวนผู้ป่วยใน Dataset
* รองรับหลายโรงพยาบาล
* พัฒนา Disease Pattern Modeling
* เชื่อมต่อกับ Electronic Health Records (EHR)
* พัฒนา Real-Time Clinical Decision Support System

⸻

Disclaimer

ระบบนี้ถูกพัฒนาขึ้นเพื่อการวิจัยและการสนับสนุนการตัดสินใจทางคลินิกเท่านั้น

ผลลัพธ์จากระบบไม่สามารถใช้แทนการวินิจฉัยหรือการรักษาโดยแพทย์ได้