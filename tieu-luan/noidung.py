# -*- coding: utf-8 -*-
"""Nội dung tiểu luận Triết học – Nguyễn Đoàn Diễm Ngọc (MSHV: 25C56077).

Quy ước định dạng nội dòng:
  **...**  in đậm      *...*  in nghiêng
  _{...}   chỉ số dưới  ^{...} chỉ số trên
  [@khoa] hoặc [@khoa1; @khoa2]  trích dẫn; được đánh số tự động theo danh mục TLTK.
Các khối nội dung (xem các tệp chuong_*.py):
  ("h1", tiêu đề chương/phần, tiêu đề trong mục lục)
  ("h2", tiêu đề mục)        ("h3", tiêu đề tiểu mục)
  ("sub", tiêu đề nhỏ không đưa vào mục lục)
  ("p", đoạn văn)            ("table", khóa bảng)      ("figure", khóa hình)
"""
from chuong_0_mo_dau import BLOCKS as MO_DAU
from chuong_1 import BLOCKS as CHUONG_1
from chuong_2 import BLOCKS as CHUONG_2
from chuong_3 import BLOCKS as CHUONG_3
from chuong_4 import BLOCKS as CHUONG_4
from ket_luan import BLOCKS as KET_LUAN

HO_TEN = "NGUYỄN ĐOÀN DIỄM NGỌC"
MSHV = "25C56077"
NGANH = "Hóa học"
NAM = "2026"

TEN_DE_TAI_DONG = [
    "VẬN DỤNG CẶP PHẠM TRÙ",
    "BẢN CHẤT VÀ HIỆN TƯỢNG",
    "TRONG ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME",
    "CỦA HỢP CHẤT THIÊN NHIÊN",
]

NOI_DUNG = MO_DAU + CHUONG_1 + CHUONG_2 + CHUONG_3 + CHUONG_4 + KET_LUAN

CHU_VIET_TAT = [
    ("[E], [S]", "Nồng độ enzyme, nồng độ cơ chất"),
    ("CETSA", "Phép thử dịch chuyển nhiệt trong tế bào (Cellular thermal shift assay)"),
    ("DLS", "Tán xạ ánh sáng động (Dynamic light scattering)"),
    ("DMSO", "Dimethyl sulfoxid"),
    ("DTNB", "Acid 5,5'-dithiobis(2-nitrobenzoic) (thuốc thử Ellman)"),
    ("FDA", "Cơ quan Quản lý Thực phẩm và Dược phẩm Hoa Kỳ (Food and Drug Administration)"),
    ("HMG-CoA", "3-Hydroxy-3-methylglutaryl-coenzyme A"),
    ("HPLC", "Sắc ký lỏng hiệu năng cao (High-performance liquid chromatography)"),
    ("IC_{50}", "Nồng độ ức chế 50% hoạt tính (Half-maximal inhibitory concentration)"),
    ("IMPs", "Thuốc vạn năng chuyển hóa không hợp lệ (Invalid metabolic panaceas)"),
    ("ITC", "Nhiệt lượng kế chuẩn độ đẳng nhiệt (Isothermal titration calorimetry)"),
    ("K_{i}", "Hằng số ức chế (Inhibition constant)"),
    ("K_{m}", "Hằng số Michaelis"),
    ("MIABE", "Thông tin tối thiểu về một thực thể có hoạt tính sinh học "
              "(Minimum information about a bioactive entity)"),
    ("NMR", "Cộng hưởng từ hạt nhân (Nuclear magnetic resonance)"),
    ("PAINS", "Hợp chất gây nhiễu đa phép thử (Pan-assay interference compounds)"),
    ("pNPG", "*p*-Nitrophenyl-α-D-glucopyranosid"),
    ("qNMR", "Cộng hưởng từ hạt nhân định lượng (Quantitative NMR)"),
    ("SAR", "Quan hệ cấu trúc – hoạt tính (Structure–activity relationship)"),
    ("SPR", "Cộng hưởng plasmon bề mặt (Surface plasmon resonance)"),
    ("STAR", "Quan hệ cấu trúc – phơi nhiễm mô/chọn lọc – hoạt tính "
             "(Structure–tissue exposure/selectivity–activity relationship)"),
    ("STD-NMR", "NMR chênh lệch truyền bão hòa (Saturation transfer difference NMR)"),
    ("TPEN", "N,N,N',N'-Tetrakis(2-pyridylmethyl)ethylendiamin (chất tạo phức kim loại)"),
]

# ------------------------------------------------------------------ BẢNG, HÌNH
# Mỗi bảng: tiêu đề, nguồn, độ rộng cột (cm, tổng 15,5), các hàng (hàng đầu là tiêu đề cột).
# Trong ô, "\n" tạo xuống dòng; dòng đầu của cột đầu được in đậm.
BANG = {
    "B1_1": {
        "tieu_de": "Bảng 1.1. Mối liên hệ giữa cặp phạm trù bản chất – hiện tượng với các cặp "
                   "phạm trù khác",
        "nguon": "Nguồn: Học viên tổng hợp trên cơ sở [@bgd2015; @bgd2021].",
        "rong": [3.6, 6.2, 5.7],
        "hang": [
            ("Cặp phạm trù", "Điểm liên hệ với bản chất – hiện tượng",
             "Biểu hiện trong đánh giá hoạt tính"),
            ("Cái chung – cái riêng",
             "Bản chất thuộc về cái chung; hiện tượng mang tính cá biệt",
             "Một giá trị IC_{50} là cái riêng; xu hướng SAR của cả dãy hợp chất gần với cái chung"),
            ("Nguyên nhân – kết quả",
             "Một hiện tượng có thể là kết quả của nhiều nguyên nhân khác nhau",
             "Giảm tín hiệu có thể do ức chế đặc hiệu, kết tập, nhiễu quang học hoặc tạp chất"),
            ("Tất nhiên – ngẫu nhiên",
             "Bản chất gắn với cái tất nhiên; hiện tượng chứa cả yếu tố ngẫu nhiên",
             "Kết quả lặp lại qua nhiều hệ thử là dấu hiệu của cái tất nhiên"),
            ("Nội dung – hình thức",
             "Hình thức biểu hiện có thể không tương ứng với nội dung",
             "Cảnh báo cấu trúc PAINS là dấu hiệu hình thức, không thay thế thực nghiệm"),
            ("Khả năng – hiện thực",
             "Hiện tượng in vitro mới chỉ ra một khả năng",
             "Một chất có hoạt tính in vitro mới là khả năng, chưa phải hiện thực của một thuốc"),
        ],
    },
    "B2_1": {
        "tieu_de": "Bảng 2.1. Các thuyết acid – base như những cấp độ nhận thức bản chất",
        "nguon": "Nguồn: Học viên tổng hợp từ [@brock1992; @bronsted1923; @lowry1923; @lewis1923].",
        "rong": [3.3, 4.4, 4.2, 3.6],
        "hang": [
            ("Thuyết", "Bản chất của tính acid", "Phạm vi hiện tượng được giải thích",
             "Giới hạn"),
            ("Arrhenius\n(cuối thế kỷ XIX)",
             "Chất phân ly trong nước tạo ion H^{+}",
             "Dung dịch nước; phản ứng trung hòa",
             "Không áp dụng cho dung môi khác nước; khó giải thích tính base của NH_{3}"),
            ("Brønsted – Lowry\n(1923)",
             "Chất cho proton; base là chất nhận proton",
             "Cặp acid – base liên hợp; dung môi không phải nước",
             "Chỉ bao quát các quá trình trao đổi proton"),
            ("Lewis\n(1923)",
             "Chất nhận cặp electron; base là chất cho cặp electron",
             "BF_{3}, AlCl_{3}, ion kim loại, phức chất",
             "Khó định lượng độ mạnh bằng một thang duy nhất"),
        ],
    },
    "B3_1": {
        "tieu_de": "Bảng 3.1. Một số thuốc ức chế enzyme có nguồn gốc từ hợp chất thiên nhiên",
        "nguon": "Nguồn: Học viên tổng hợp từ [@wehmeier2004; @endo2010; @heinrich2004; @weibel1987; "
                 "@cushman1991].",
        "rong": [3.0, 3.6, 5.0, 3.9],
        "hang": [
            ("Thuốc", "Enzyme đích", "Nguồn gốc", "Ghi chú"),
            ("Acarbose", "α-Glucosidase ruột",
             "Sản xuất bằng lên men chủng *Actinoplanes* sp. SE50",
             "Dùng trong điều trị đái tháo đường type 2 từ năm 1990"),
            ("Lovastatin và các statin", "HMG-CoA reductase",
             "Chất chuyển hóa của nấm; compactin từ *Penicillium citrinum*, lovastatin từ "
             "*Aspergillus terreus*",
             "Hạ cholesterol máu, giảm biến cố mạch vành"),
            ("Galantamine", "Acetylcholinesterase",
             "Alcaloid của các loài họ Thủy tiên (*Galanthus*, *Narcissus*, *Leucojum*)",
             "Điều trị bệnh Alzheimer"),
            ("Orlistat", "Lipase tụy",
             "Dẫn xuất của lipstatin từ *Streptomyces toxytricini*",
             "Lipstatin: IC_{50} = 0,14 μM, không ức chế phospholipase A_{2} và trypsin"),
            ("Captopril", "Enzyme chuyển angiotensin",
             "Thiết kế dựa trên các peptide từ nọc rắn *Bothrops jararaca*",
             "Điều trị tăng huyết áp"),
        ],
    },
    "B3_2": {
        "tieu_de": "Bảng 3.2. Một số phép thử ức chế enzyme thường dùng và nguy cơ giả tượng",
        "nguon": "Nguồn: Học viên tổng hợp; nguyên lý phép thử acetylcholinesterase theo [@ellman1961]; "
                 "sự khác biệt giữa enzyme mô hình và enzyme đích theo [@oki1999; @mann2018]; nguy cơ kết "
                 "tập và gây nhiễu theo [@mcgovern2002; @baell2014].",
        "rong": [2.9, 3.4, 5.0, 4.2],
        "hang": [
            ("Enzyme", "Nguồn enzyme thường dùng", "Nguyên lý phát hiện",
             "Nguy cơ giả tượng đặc thù"),
            ("α-Glucosidase", "Nấm men *Saccharomyces cerevisiae*",
             "pNPG → *p*-nitrophenol; đo quang ở vùng 400–405 nm",
             "Enzyme nấm men khác enzyme ruột động vật có vú"),
            ("Acetylcholin-esterase", "Cá chình điện *Electrophorus electricus*",
             "Phương pháp Ellman: thiocholin phản ứng với DTNB; đo quang ở 412 nm",
             "Hợp chất phản ứng với nhóm thiol hoặc hấp thụ ở 412 nm"),
            ("Tyrosinase", "Nấm *Agaricus bisporus*",
             "L-DOPA → dopachrome; đo quang ở 475 nm",
             "Enzyme nấm khác tyrosinase người"),
            ("Xanthine oxidase", "Sữa bò",
             "Xanthine → acid uric; đo quang ở vùng 290–295 nm",
             "Hợp chất hấp thụ mạnh vùng tử ngoại"),
            ("Lipase tụy", "Tụy lợn",
             "Ester của *p*-nitrophenol → *p*-nitrophenol; đo quang ở vùng 405 nm",
             "Kết tập; tương tác với bề mặt cơ chất kỵ nước"),
        ],
    },
    "B4_1": {
        "tieu_de": "Bảng 4.1. Quy trình đánh giá hoạt tính ức chế enzyme theo các cấp độ tiếp cận "
                   "bản chất",
        "nguon": "Nguồn: Học viên tổng hợp và đề xuất trên cơ sở [@aldrich2017; @capuzzi2017; "
                 "@cheng1973; @copeland2013; @feng2006; @hermann2013; @irwin2015; @jafari2014; "
                 "@mcgovern2002; @oki1999; @pauli2014; @shoichet2006; @warren2006].",
        "rong": [5.3, 5.9, 4.3],
        "hang": [
            ("Cấp độ và câu hỏi về bản chất", "Phép thử, kiểm chứng", "Giả tượng cần loại trừ"),
            ("1. Tín hiệu sơ cấp\nTín hiệu có lặp lại, có thuộc về chính hợp chất?",
             "Lặp lại độc lập; mẫu trắng không enzyme; độ tinh khiết (HPLC, qNMR)",
             "Hấp thụ, huỳnh quang nội tại; tạp chất hữu cơ và vô cơ"),
            ("2. Liều – đáp ứng\nTác dụng phụ thuộc nồng độ ra sao?",
             "Đường cong đầy đủ; báo cáo [E], [S]/K_{m}, % DMSO, thời gian ủ",
             "Đường cong dốc bất thường; phụ thuộc mạnh vào điều kiện"),
            ("3. Tính đặc hiệu\nỨc chế có đặc hiệu với enzyme đích?",
             "Chất hoạt động bề mặt không ion; tăng [E]; DLS; TPEN; enzyme không liên quan",
             "Kết tập keo; ion kim loại; phản ứng cộng hóa trị, oxy hóa – khử"),
            ("4. Cơ chế\nKiểu ức chế, K_{i}, tính thuận nghịch?",
             "Động học enzyme; pha loãng nhanh; ITC, SPR, STD-NMR; docking đối chiếu dữ liệu "
             "động học",
             "Suy diễn cơ chế từ điểm số docking"),
            ("5. Quan hệ cấu trúc – hoạt tính\nHoạt tính có biến đổi nhất quán theo cấu trúc?",
             "Dãy hợp chất đồng loại từ phân lập hoặc bán tổng hợp",
             "SAR “phẳng”, không giải thích được"),
            ("6. Tương ứng với đích sinh học\nTác dụng có trên đích ở người, trong tế bào, cơ thể?",
             "Enzyme động vật có vú hoặc enzyme người tái tổ hợp; CETSA; dược động học; *in vivo*",
             "Hoạt tính chỉ có trên mô hình không tương đồng"),
        ],
    },
    "B4_2": {
        "tieu_de": "Bảng 4.2. Các kịch bản kết quả trong tình huống minh họa và kết luận "
                   "tương ứng",
        "nguon": "Ghi chú: Tình huống giả định, dùng để minh họa phương pháp luận; không phải dữ liệu "
                 "thực nghiệm.",
        "rong": [2.6, 5.4, 4.2, 3.3],
        "hang": [
            ("Kịch bản", "Kết quả quan sát", "Diễn giải", "Kết luận được phép"),
            ("A", "Hoạt tính giảm mạnh khi thêm chất hoạt động bề mặt; DLS phát hiện hạt keo",
             "Giả tượng do kết tập", "Không phải chất ức chế đặc hiệu"),
            ("B", "Hoạt tính bền với chất hoạt động bề mặt nhưng không có trên α-glucosidase ruột "
                  "chuột",
             "Hiện tượng gắn với mô hình nấm men", "Chỉ ức chế enzyme nấm men"),
            ("C", "Hoạt tính bền, có trên enzyme động vật có vú, ức chế cạnh tranh, SAR nhất quán",
             "Tiếp cận được bản chất cấp hai – cấp ba", "Chất ức chế đặc hiệu, cần đánh giá tiếp "
                                                        "*in vivo*"),
        ],
    },
}

HINH = {
    "H4_1": {
        "tieu_de": "Hình 4.1. Sơ đồ tiến trình từ hiện tượng đến bản chất trong đánh giá hoạt tính "
                   "ức chế enzyme",
        "tep": "hinh_4_1.png",
        "rong_cm": 15.0,
    },
}

# --------------------------------------------------------- TÀI LIỆU THAM KHẢO
# Xếp theo ngôn ngữ; trong mỗi nhóm theo thứ tự chữ cái tên tác giả/cơ quan.
TAI_LIEU_VIET = [
    ("bgd2015", "Bộ Giáo dục và Đào tạo (2015), *Giáo trình Triết học (Dùng cho khối không chuyên ngành "
                "Triết học trình độ đào tạo thạc sĩ, tiến sĩ các ngành khoa học tự nhiên, công nghệ)*, "
                "NXB Chính trị quốc gia – Sự thật, Hà Nội."),
    ("bgd2021", "Bộ Giáo dục và Đào tạo (2021), *Giáo trình Triết học Mác – Lênin (Dành cho bậc đại học "
                "hệ không chuyên lý luận chính trị)*, NXB Chính trị quốc gia Sự thật, Hà Nội."),
    ("lenin18", "V.I. Lênin (2005), *Toàn tập*, tập 18 (Chủ nghĩa duy vật và chủ nghĩa kinh nghiệm phê "
                "phán), NXB Chính trị quốc gia, Hà Nội."),
    ("lenin29", "V.I. Lênin (2006), *Toàn tập*, tập 29 (Bút ký triết học), NXB Chính trị quốc gia, "
                "Hà Nội."),
    ("marx25", "C. Mác và Ph. Ăngghen (1994), *Toàn tập*, tập 25, phần II, NXB Chính trị quốc gia, "
               "Hà Nội."),
]

TAI_LIEU_ANH = [
    ("aldrich2017", "Aldrich C., Bertozzi C., Georg G.I., et al. (2017), “The ecstasy and agony of "
                    "assay interference compounds”, *Journal of Medicinal Chemistry*, 60(6), "
                    "pp. 2165–2168. DOI: 10.1021/acs.jmedchem.7b00229."),
    ("atanasov2021", "Atanasov A.G., Zotchev S.B., Dirsch V.M., International Natural Product Sciences "
                     "Taskforce, Supuran C.T. (2021), “Natural products in drug discovery: advances "
                     "and opportunities”, *Nature Reviews Drug Discovery*, 20(3), pp. 200–216. "
                     "DOI: 10.1038/s41573-020-00114-z."),
    ("baell2010", "Baell J.B., Holloway G.A. (2010), “New substructure filters for removal of pan "
                  "assay interference compounds (PAINS) from screening libraries and for their "
                  "exclusion in bioassays”, *Journal of Medicinal Chemistry*, 53(7), pp. 2719–2740. "
                  "DOI: 10.1021/jm901137j."),
    ("baell2014", "Baell J., Walters M.A. (2014), “Chemistry: Chemical con artists foil drug "
                  "discovery”, *Nature*, 513(7519), pp. 481–483. DOI: 10.1038/513481a."),
    ("begley2012", "Begley C.G., Ellis L.M. (2012), “Drug development: Raise standards for "
                   "preclinical cancer research”, *Nature*, 483(7391), pp. 531–533. "
                   "DOI: 10.1038/483531a."),
    ("bisson2016", "Bisson J., McAlpine J.B., Friesen J.B., Chen S.-N., Graham J., Pauli G.F. (2016), "
                   "“Can invalid bioactives undermine natural product-based drug discovery?”, "
                   "*Journal of Medicinal Chemistry*, 59(5), pp. 1671–1690. "
                   "DOI: 10.1021/acs.jmedchem.5b01009."),
    ("blake1965", "Blake C.C., Koenig D.F., Mair G.A., North A.C., Phillips D.C., Sarma V.R. (1965), "
                  "“Structure of hen egg-white lysozyme: a three-dimensional Fourier synthesis at "
                  "2 Å resolution”, *Nature*, 206(4986), pp. 757–761. DOI: 10.1038/206757a0."),
    ("brock1992", "Brock W.H. (1992), *The Fontana History of Chemistry*, Fontana Press, London."),
    ("bronsted1923", "Brønsted J.N. (1923), “Einige Bemerkungen über den Begriff der Säuren und "
                     "Basen”, *Recueil des Travaux Chimiques des Pays-Bas*, 42(8), pp. 718–728. "
                     "DOI: 10.1002/recl.19230420815."),
    ("capuzzi2017", "Capuzzi S.J., Muratov E.N., Tropsha A. (2017), “Phantom PAINS: Problems with "
                    "the utility of alerts for pan-assay interference compounds”, *Journal of "
                    "Chemical Information and Modeling*, 57(3), pp. 417–427. "
                    "DOI: 10.1021/acs.jcim.6b00465."),
    ("cheng1973", "Cheng Y., Prusoff W.H. (1973), “Relationship between the inhibition constant "
                  "(K_{1}) and the concentration of inhibitor which causes 50 per cent inhibition "
                  "(I_{50}) of an enzymatic reaction”, *Biochemical Pharmacology*, 22(23), "
                  "pp. 3099–3108. DOI: 10.1016/0006-2952(73)90196-2."),
    ("copeland2013", "Copeland R.A. (2013), *Evaluation of Enzyme Inhibitors in Drug Discovery: A "
                     "Guide for Medicinal Chemists and Pharmacologists*, 2nd ed., John Wiley & Sons, "
                     "Hoboken, NJ. DOI: 10.1002/9781118540398."),
    ("cushman1991", "Cushman D.W., Ondetti M.A. (1991), “History of the design of captopril and "
                    "related inhibitors of angiotensin converting enzyme”, *Hypertension*, 17(4), "
                    "pp. 589–592. DOI: 10.1161/01.hyp.17.4.589."),
    ("ellman1961", "Ellman G.L., Courtney K.D., Andres V., Featherstone R.M. (1961), “A new and rapid "
                   "colorimetric determination of acetylcholinesterase activity”, *Biochemical "
                   "Pharmacology*, 7, pp. 88–95. DOI: 10.1016/0006-2952(61)90145-9."),
    ("endo2010", "Endo A. (2010), “A historical perspective on the discovery of statins”, "
                 "*Proceedings of the Japan Academy, Series B, Physical and Biological Sciences*, "
                 "86(5), pp. 484–493. DOI: 10.2183/pjab.86.484."),
    ("feng2006", "Feng B.Y., Shoichet B.K. (2006), “A detergent-based assay for the detection of "
                 "promiscuous inhibitors”, *Nature Protocols*, 1(2), pp. 550–553. "
                 "DOI: 10.1038/nprot.2006.77."),
    ("feng2007", "Feng B.Y., Simeonov A., Jadhav A., Babaoglu K., Inglese J., Shoichet B.K., "
                 "Austin C.P. (2007), “A high-throughput screen for aggregation-based inhibition in "
                 "a large compound library”, *Journal of Medicinal Chemistry*, 50(10), "
                 "pp. 2385–2390. DOI: 10.1021/jm061317y."),
    ("heinrich2004", "Heinrich M., Teoh H.L. (2004), “Galanthamine from snowdrop – the development of "
                     "a modern drug against Alzheimer's disease from local Caucasian knowledge”, "
                     "*Journal of Ethnopharmacology*, 92(2–3), pp. 147–162. "
                     "DOI: 10.1016/j.jep.2004.02.012."),
    ("hermann2013", "Hermann J.C., Chen Y., Wartchow C., et al. (2013), “Metal impurities cause false "
                    "positives in high-throughput screening campaigns”, *ACS Medicinal Chemistry "
                    "Letters*, 4(2), pp. 197–200. DOI: 10.1021/ml3003296."),
    ("irwin2015", "Irwin J.J., Duan D., Torosyan H., et al. (2015), “An aggregation advisor for "
                  "ligand discovery”, *Journal of Medicinal Chemistry*, 58(17), pp. 7076–7087. "
                  "DOI: 10.1021/acs.jmedchem.5b01105."),
    ("ito2010", "Ito T., Ando H., Suzuki T., et al. (2010), “Identification of a primary target of "
                "thalidomide teratogenicity”, *Science*, 327(5971), pp. 1345–1350. "
                "DOI: 10.1126/science.1177319."),
    ("jafari2014", "Jafari R., Almqvist H., Axelsson H., Ignatushchenko M., Lundbäck T., Nordlund P., "
                   "Martinez Molina D. (2014), “The cellular thermal shift assay for evaluating drug "
                   "target interactions in cells”, *Nature Protocols*, 9(9), pp. 2100–2122. "
                   "DOI: 10.1038/nprot.2014.138."),
    ("johnson2011", "Johnson K.A., Goody R.S. (2011), “The original Michaelis constant: translation of "
                    "the 1913 Michaelis–Menten paper”, *Biochemistry*, 50(39), pp. 8264–8269. "
                    "DOI: 10.1021/bi201284u."),
    ("koshland1958", "Koshland D.E. (1958), “Application of a theory of enzyme specificity to protein "
                     "synthesis”, *Proceedings of the National Academy of Sciences of the United States of America*, "
                     "44(2), "
                     "pp. 98–104. DOI: 10.1073/pnas.44.2.98."),
    ("lewis1923", "Lewis G.N. (1923), *Valence and the Structure of Atoms and Molecules*, The Chemical "
                  "Catalog Company, New York."),
    ("lowry1923", "Lowry T.M. (1923), “The uniqueness of hydrogen”, *Journal of the Society of "
                  "Chemical Industry*, 42(3), pp. 43–47. DOI: 10.1002/jctb.5000420302."),
    ("mann2018", "Mann T., Gerwat W., Batzer J., et al. (2018), “Inhibition of human tyrosinase "
                 "requires molecular motifs distinctively different from mushroom tyrosinase”, "
                 "*Journal of Investigative Dermatology*, 138(7), pp. 1601–1608. "
                 "DOI: 10.1016/j.jid.2018.01.019."),
    ("mcgovern2002", "McGovern S.L., Caselli E., Grigorieff N., Shoichet B.K. (2002), “A common "
                     "mechanism underlying promiscuous inhibitors from virtual and high-throughput "
                     "screening”, *Journal of Medicinal Chemistry*, 45(8), pp. 1712–1722. "
                     "DOI: 10.1021/jm010533y."),
    ("moseley1913", "Moseley H.G.J. (1913), “The high-frequency spectra of the elements”, "
                    "*The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, "
                    "Series 6, 26(156), pp. 1024–1034. "
                    "DOI: 10.1080/14786441308635052."),
    ("nelson2017", "Nelson K.M., Dahlin J.L., Bisson J., Graham J., Pauli G.F., Walters M.A. (2017), "
                   "“The essential medicinal chemistry of curcumin”, *Journal of Medicinal "
                   "Chemistry*, 60(5), pp. 1620–1637. DOI: 10.1021/acs.jmedchem.6b00975."),
    ("newman2020", "Newman D.J., Cragg G.M. (2020), “Natural products as sources of new drugs over "
                   "the nearly four decades from 01/1981 to 09/2019”, *Journal of Natural "
                   "Products*, 83(3), pp. 770–803. DOI: 10.1021/acs.jnatprod.9b01285."),
    ("oki1999", "Oki T., Matsui T., Osajima Y. (1999), “Inhibitory effect of α-glucosidase inhibitors "
                "varies according to its origin”, *Journal of Agricultural and Food Chemistry*, "
                "47(2), pp. 550–553. DOI: 10.1021/jf980788t."),
    ("orchard2011", "Orchard S., Al-Lazikani B., Bryant S., et al. (2011), “Minimum information about "
                    "a bioactive entity (MIABE)”, *Nature Reviews Drug Discovery*, 10(9), "
                    "pp. 661–669. DOI: 10.1038/nrd3503."),
    ("pauli2014", "Pauli G.F., Chen S.-N., Simmler C., et al. (2014), “Importance of purity "
                  "evaluation and the potential of quantitative ^{1}H NMR as a purity assay”, "
                  "*Journal of Medicinal Chemistry*, 57(22), pp. 9220–9231. "
                  "DOI: 10.1021/jm500734a."),
    ("prinz2011", "Prinz F., Schlange T., Asadullah K. (2011), “Believe it or not: how much can we "
                  "rely on published data on potential drug targets?”, *Nature Reviews Drug "
                  "Discovery*, 10(9), p. 712. DOI: 10.1038/nrd3439-c1."),
    ("shoichet2006", "Shoichet B.K. (2006), “Screening in a spirit haunted world”, *Drug Discovery "
                     "Today*, 11(13–14), pp. 607–615. DOI: 10.1016/j.drudis.2006.05.014."),
    ("sun2022", "Sun D., Gao W., Hu H., Zhou S. (2022), “Why 90% of clinical drug development fails "
                "and how to improve it?”, *Acta Pharmaceutica Sinica B*, 12(7), pp. 3049–3062. "
                "DOI: 10.1016/j.apsb.2022.02.002."),
    ("vargesson2015", "Vargesson N. (2015), “Thalidomide-induced teratogenesis: history and "
                      "mechanisms”, *Birth Defects Research Part C: Embryo Today: Reviews*, 105(2), "
                      "pp. 140–156. DOI: 10.1002/bdrc.21096."),
    ("warren2006", "Warren G.L., Andrews C.W., Capelli A.M., et al. (2006), “A critical assessment of "
                   "docking programs and scoring functions”, *Journal of Medicinal Chemistry*, 49(20), "
                   "pp. 5912–5931. DOI: 10.1021/jm050362n."),
    ("wehmeier2004", "Wehmeier U.F., Piepersberg W. (2004), “Biotechnology and molecular biology of "
                     "the α-glucosidase inhibitor acarbose”, *Applied Microbiology and "
                     "Biotechnology*, 63(6), pp. 613–625. DOI: 10.1007/s00253-003-1477-2."),
    ("weibel1987", "Weibel E.K., Hadvary P., Hochuli E., Kupfer E., Lengsfeld H. (1987), “Lipstatin, "
                   "an inhibitor of pancreatic lipase, produced by *Streptomyces toxytricini*. I. "
                   "Producing organism, fermentation, isolation and biological activity”, *The "
                   "Journal of Antibiotics*, 40(8), pp. 1081–1085. DOI: 10.7164/antibiotics.40.1081."),
]
