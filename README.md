ariant="document" id="78452"}
# MetaboRecovery AI
## ระบบปัญญาประดิษฐ์เพื่อช่วยประเมินการฟื้นตัวหลังการผ่าตัดจากข้อมูลเมตาโบโลมิกส์ (Metabolomics-Based Clinical Decision Support System)

---

# ที่มาและความสำคัญของโครงการ

การประเมินการฟื้นตัวของผู้ป่วยหลังการผ่าตัดเป็นหนึ่งในความท้าทายสำคัญทางการแพทย์ เนื่องจากผู้ป่วยแต่ละรายมีการตอบสนองต่อการรักษาแตกต่างกัน แม้ว่าจะได้รับการรักษาในรูปแบบเดียวกันก็ตาม

ปัจจุบันเทคโนโลยี Metabolomics สามารถวิเคราะห์สารเมตาโบไลต์ภายในร่างกาย ซึ่งสะท้อนถึงสภาวะทางชีวภาพและกระบวนการฟื้นตัวของผู้ป่วยได้อย่างละเอียด ทำให้สามารถนำข้อมูลดังกล่าวมาประยุกต์ใช้ร่วมกับปัญญาประดิษฐ์ (Artificial Intelligence) เพื่อคาดการณ์ผลลัพธ์ทางคลินิกได้อย่างมีประสิทธิภาพ

โครงการ MetaboRecovery AI จึงถูกพัฒนาขึ้นเพื่อสร้างระบบ Clinical Decision Support System (CDSS) ที่สามารถช่วยประเมินความเสี่ยงในการฟื้นตัวของผู้ป่วยหลังการผ่าตัด พร้อมอธิบายเหตุผลของการตัดสินใจของโมเดลผ่านการวิเคราะห์ Biomarker ที่สำคัญ

---

# วัตถุประสงค์

1. พัฒนาโมเดล Machine Learning สำหรับคาดการณ์ผลการฟื้นตัวหลังการผ่าตัด

2. วิเคราะห์ Biomarker ที่มีผลต่อการฟื้นตัวของผู้ป่วย

3. สร้างระบบ Clinical AI Report เพื่อช่วยอธิบายผลการทำนายของโมเดล

4. พัฒนาต้นแบบ Clinical Decision Support Platform สำหรับบุคลากรทางการแพทย์

---

# ข้อมูลที่ใช้ในการศึกษา

## Dataset

ข้อมูลผู้ป่วยทั้งหมด

47 ราย

แบ่งเป็น

- Poor Recovery จำนวน 24 ราย
- Fast Recovery จำนวน 23 ราย

ข้อมูลประกอบด้วย

- Clinical Score
- Glycine
- Creatinine
- Amino Acid Metabolites
- Ketone Body Metabolites
- Metabolomics Biomarkers อื่น ๆ

---

# วิธีดำเนินงาน

## 1. Data Preparation

- ทำความสะอาดข้อมูล
- คัดเลือกตัวแปรสำคัญ
- เตรียมข้อมูลสำหรับ Machine Learning

## 2. Feature Selection

วิเคราะห์และคัดเลือก Biomarker ที่มีความสัมพันธ์กับผลการฟื้นตัว

Biomarker สุดท้ายที่ถูกเลือก ได้แก่

1. clinical_score
2. glycine_preop
3. creatinine_preop
4. L-allo-Isoleucine_3m
5. L-glutamine_3m
6. (R)-3-Hydroxybutyric acid_3m
7. L-valine_preop

---

## 3. Machine Learning Model

โมเดลที่ใช้

Random Forest Classifier

Parameter

- n_estimators = 100
- max_depth = 3
- random_state = 42

Validation Method

- Stratified 5-Fold Cross Validation

---

# ผลการทดลอง

## Model Performance

Accuracy

91.56%

Cross Validation Scores

- 90.0%
- 90.0%
- 88.9%
- 100.0%
- 88.9%

Training Accuracy

97.87%

---

## Biomarker Importance

Biomarker ที่มีผลต่อการตัดสินใจของโมเดลมากที่สุด

| Biomarker | Importance |
|------------|------------|
| clinical_score | 37.4% |
| glycine_preop | 17.5% |
| L-glutamine_3m | 11.0% |
| L-allo-Isoleucine_3m | 10.5% |
| creatinine_preop | 10.5% |
| L-valine_preop | 7.9% |
| (R)-3-Hydroxybutyric acid_3m | 5.2% |

---

# ระบบ Clinical AI Report

ระบบสามารถสร้างรายงานอัตโนมัติสำหรับผู้ป่วยแต่ละราย ประกอบด้วย

## Patient Information

- Patient ID
- วันที่วิเคราะห์
- Prediction Result
- Confidence Score

## Biomarker Assessment

สำหรับ Biomarker ที่ผิดปกติ ระบบจะแสดง

- Patient Value
- Population Mean
- Z-Score
- Clinical Significance
- Clinical Interpretation
- Associated Conditions

## AI Condition Statement

สรุปเหตุผลของการทำนายโดยอ้างอิงจาก Biomarker สำคัญ

## Clinical Risk Summary

- Recovery Risk
- Metabolic Risk
- Overall Status
- AI Risk Score

## Final Assessment

สรุปผลทางคลินิกที่เข้าใจง่ายสำหรับบุคลากรทางการแพทย์

---

# Dashboard Prototype

ต้นแบบแพลตฟอร์มประกอบด้วย

## Recovery Analytics Dashboard

แสดง

- Model Accuracy
- Patient Count
- Recovery Distribution
- Biomarker Importance
- PCA Recovery Clusters

## Patient Analysis

สำหรับวิเคราะห์ผู้ป่วยรายบุคคล

## Clinical Report

สำหรับแสดงรายงานการวิเคราะห์แบบละเอียด

## SHAP Explorer

สำหรับอธิบายการตัดสินใจของโมเดล

---

# จุดเด่นของโครงการ

- ใช้ข้อมูล Metabolomics จริงในการวิเคราะห์
- มีความแม่นยำ 91.56%
- สามารถอธิบายเหตุผลของการทำนายได้
- แสดงผลในรูปแบบ Clinical Report
- มี Dashboard สำหรับใช้งานจริง
- สามารถพัฒนาเป็น Clinical Decision Support Platform ในอนาคต

---

# ผลลัพธ์ที่คาดว่าจะได้รับ

1. ระบบต้นแบบสำหรับประเมินการฟื้นตัวหลังการผ่าตัด

2. เครื่องมือช่วยสสนุนการตัดสินใจทางคลินิก

3. แนวทางการประยุกต์ใช้ Metabolomics ร่วมกับ Artificial Intelligence ในงานทางการแพทย์

4. ต้นแบบแพลตฟอร์ม HealthTech ที่สามารถต่อยอดสู่การใช้งานจริงได้

ข้อจำกัด

โครงการอยู่ในระดับต้นแบบ (Prototype)

ข้อมูลผู้ป่วยมีจำนวน 47 ราย ซึ่งยังจำเป็นต้องมีการเก็บข้อมูลเพิ่มเติมเพื่อเพิ่มความสามารถในการใช้งานในระดับคลินิกจริง

ผลลัพธ์ของระบบมีวัตถุประสงค์เพื่อการวิจัยและการสนับสนุนการตัดสินใจเท่านั้น ไม่สามารถใช้แทนการวินิจฉัยโดยแพทย์ได้