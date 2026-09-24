# -*- coding: utf-8 -*-
"""Nội dung tiểu luận Triết học – Nguyễn Đoàn Diễm Ngọc (MSHV: 25C56077).

Quy ước định dạng nội dòng:
  **...**  in đậm      *...*  in nghiêng
  _{...}   chỉ số dưới  ^{...} chỉ số trên
Các khối nội dung:
  ("h1", tiêu đề chương/phần, tiêu đề trong mục lục)
  ("h2", tiêu đề mục)        ("h3", tiêu đề tiểu mục)
  ("sub", tiêu đề nhỏ không đưa vào mục lục)
  ("p", đoạn văn)            ("table", khóa bảng)
"""

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

CHU_VIET_TAT = [
    ("[E], [S]", "Nồng độ enzyme, nồng độ cơ chất"),
    ("CETSA", "Phép thử dịch chuyển nhiệt trong tế bào (Cellular thermal shift assay)"),
    ("DLS", "Tán xạ ánh sáng động (Dynamic light scattering)"),
    ("DMSO", "Dimethyl sulfoxid"),
    ("FDA", "Cơ quan Quản lý Thực phẩm và Dược phẩm Hoa Kỳ (Food and Drug Administration)"),
    ("HPLC", "Sắc ký lỏng hiệu năng cao (High-performance liquid chromatography)"),
    ("IC_{50}", "Nồng độ ức chế 50% hoạt tính (Half-maximal inhibitory concentration)"),
    ("IMPs", "Thuốc vạn năng chuyển hóa không hợp lệ (Invalid metabolic panaceas)"),
    ("ITC", "Nhiệt lượng kế chuẩn độ đẳng nhiệt (Isothermal titration calorimetry)"),
    ("K_{i}", "Hằng số ức chế (Inhibition constant)"),
    ("K_{m}", "Hằng số Michaelis"),
    ("NMR", "Cộng hưởng từ hạt nhân (Nuclear magnetic resonance)"),
    ("PAINS", "Hợp chất gây nhiễu đa phép thử (Pan-assay interference compounds)"),
    ("pNPG", "*p*-Nitrophenyl-α-D-glucopyranosid"),
    ("qNMR", "Cộng hưởng từ hạt nhân định lượng (Quantitative NMR)"),
    ("SAR", "Quan hệ cấu trúc – hoạt tính (Structure–activity relationship)"),
    ("SPR", "Cộng hưởng plasmon bề mặt (Surface plasmon resonance)"),
    ("STAR", "Quan hệ cấu trúc – phơi nhiễm mô/chọn lọc – hoạt tính "
             "(Structure–tissue exposure/selectivity–activity relationship)"),
    ("STD-NMR", "NMR chênh lệch truyền bão hòa (Saturation transfer difference NMR)"),
]

BANG_31_TIEU_DE = ("Bảng 3.1. Quy trình đánh giá hoạt tính ức chế enzyme "
                   "theo các cấp độ tiếp cận bản chất")
BANG_31_NGUON = ("Nguồn: Học viên tổng hợp và đề xuất trên cơ sở "
                 "[10], [11], [12], [13], [15], [16], [17], [20], [21], [23].")
# Cột 1: dòng đầu (in đậm) là tên cấp độ, dòng sau là câu hỏi về bản chất.
BANG_31 = [
    ("Cấp độ và câu hỏi về bản chất", "Phép thử, kiểm chứng", "Giả tượng cần loại trừ"),
    ("1. Tín hiệu sơ cấp\nTín hiệu có lặp lại, có thuộc về chính hợp chất?",
     "Lặp lại độc lập; mẫu trắng không enzyme; độ tinh khiết (HPLC, qNMR)",
     "Hấp thụ, huỳnh quang nội tại; tạp chất có hoạt tính"),
    ("2. Liều – đáp ứng\nTác dụng phụ thuộc nồng độ ra sao?",
     "Đường cong đầy đủ; báo cáo [E], [S]/K_{m}, % DMSO, thời gian ủ",
     "Đường cong dốc bất thường; phụ thuộc mạnh vào điều kiện"),
    ("3. Tính đặc hiệu\nỨc chế có đặc hiệu với enzyme đích?",
     "Chất hoạt động bề mặt không ion; tăng [E]; DLS; enzyme không liên quan",
     "Kết tập keo; phản ứng cộng hóa trị, oxy hóa – khử"),
    ("4. Cơ chế\nKiểu ức chế, K_{i}, tính thuận nghịch?",
     "Động học enzyme; pha loãng nhanh; ITC, SPR, STD-NMR; docking đối chiếu dữ liệu động học",
     "Suy diễn cơ chế từ điểm số docking"),
    ("5. Quan hệ cấu trúc – hoạt tính\nHoạt tính có biến đổi nhất quán theo cấu trúc?",
     "Dãy hợp chất đồng loại từ phân lập hoặc bán tổng hợp",
     "SAR “phẳng”, không giải thích được"),
    ("6. Tương ứng với đích sinh học\nTác dụng có trên đích ở người, trong tế bào, cơ thể?",
     "Enzyme động vật có vú hoặc enzyme người tái tổ hợp; CETSA; dược động học; *in vivo*",
     "Hoạt tính chỉ có trên mô hình không tương đồng"),
]

NOI_DUNG = [
    # ------------------------------------------------------------------ MỞ ĐẦU
    ("h1", "PHẦN MỞ ĐẦU", "PHẦN MỞ ĐẦU"),
    ("sub", "1. Tính cấp thiết của đề tài"),
    ("p", "Hợp chất thiên nhiên và các cấu trúc được phát triển từ chúng giữ vai trò quan trọng "
          "trong lịch sử hóa trị liệu, đặc biệt đối với các bệnh ung thư và bệnh nhiễm trùng [6]. "
          "Theo tổng quan của Newman và Cragg về các thuốc được phê duyệt trên thế giới từ năm 1981 "
          "đến năm 2019, trong lĩnh vực điều trị ung thư, 62 trong số 185 thuốc phân tử nhỏ (33,5%) "
          "có nguồn gốc trực tiếp từ hợp chất thiên nhiên; nếu tính thêm các chất tổng hợp mang dược "
          "cơ hoặc mô phỏng cấu trúc của hợp chất thiên nhiên, tỷ lệ này đạt 64,9% [19]. Sau một giai "
          "đoạn bị công nghiệp dược phẩm thu hẹp đầu tư từ thập niên 1990, hướng nghiên cứu này đang "
          "được phục hồi nhờ sự phát triển của các kỹ thuật phân tích, khai thác hệ gen và nuôi cấy vi "
          "sinh vật [6]. Tại Việt Nam, phân lập, xác định cấu trúc và đánh giá hoạt tính sinh học của "
          "hợp chất thiên nhiên là một hướng nghiên cứu chủ đạo trong đào tạo sau đại học ngành Hóa học. "
          "Trong chuỗi công việc đó, phép thử ức chế enzyme *in vitro* (α-glucosidase, "
          "acetylcholinesterase, tyrosinase, xanthine oxidase…) thường là căn cứ đầu tiên để kết luận "
          "một hợp chất có “tiềm năng” dược lý."),
    ("p", "Tuy nhiên, giá trị IC_{50} thu được từ một phép thử *in vitro* chỉ là kết quả đo, trong những "
          "điều kiện xác định, của tương tác giữa phân tử và hệ thử. Kết quả đó có thể phản ánh đúng một "
          "cơ chế ức chế đặc hiệu, nhưng cũng có thể bắt nguồn từ sự kết tập keo của phân tử, từ phản ứng "
          "không đặc hiệu với protein, từ nhiễu quang học hoặc từ sự không tương đồng giữa enzyme mô hình "
          "và đích sinh học ở người [7], [17], [20]. Việc đồng nhất tín hiệu đo được với cơ chế tác dụng "
          "dẫn đến việc lựa chọn sai ứng viên và là một trong những yếu tố góp phần vào tỷ lệ thất bại "
          "khoảng 90% của các ứng viên thuốc khi bước vào giai đoạn thử nghiệm lâm sàng [22]."),
    ("p", "Xét về phương diện triết học, đây là vấn đề về quan hệ giữa bản chất và hiện tượng. Nhận thức "
          "khoa học phải xuất phát từ hiện tượng, nhưng không được đồng nhất hiện tượng với bản chất và "
          "không được lấy giả tượng làm căn cứ. C. Mác đã chỉ ra rằng nếu hình thái biểu hiện và bản chất "
          "của sự vật trực tiếp trùng khớp với nhau thì mọi khoa học đều trở nên thừa [4]. Nhận định này "
          "xác định nhiệm vụ của khoa học là vượt qua bề mặt của các dữ kiện quan sát để phát hiện những "
          "mối liên hệ tất yếu ở bên trong. Vì vậy, việc vận dụng cặp phạm trù bản chất và hiện tượng vào "
          "hoạt động đánh giá hoạt tính sinh học có ý nghĩa cả về lý luận lẫn thực tiễn đối với người "
          "nghiên cứu hóa học hợp chất thiên nhiên. Xuất phát từ những lý do trên, học viên chọn đề tài "
          "“**Vận dụng cặp phạm trù bản chất và hiện tượng trong đánh giá hoạt tính ức chế enzyme của hợp "
          "chất thiên nhiên**” làm tiểu luận môn Triết học."),
    ("sub", "2. Mục tiêu và nhiệm vụ nghiên cứu"),
    ("p", "Mục tiêu của tiểu luận là làm rõ nội dung và ý nghĩa phương pháp luận của cặp phạm trù bản chất "
          "và hiện tượng, trên cơ sở đó đề xuất các nguyên tắc tiếp cận nhằm nâng cao độ tin cậy của các "
          "kết luận về hoạt tính ức chế enzyme của hợp chất thiên nhiên. Để đạt mục tiêu đó, tiểu luận "
          "thực hiện ba nhiệm vụ: (i) hệ thống hóa quan niệm của chủ nghĩa duy vật biện chứng về bản chất, "
          "hiện tượng và mối quan hệ giữa chúng; (ii) phân tích các biểu hiện và nguyên nhân của sự sai "
          "lệch giữa kết quả thử nghiệm và cơ chế tác dụng trong nghiên cứu hợp chất thiên nhiên; (iii) đề "
          "xuất các nguyên tắc và một quy trình đánh giá theo các cấp độ tiếp cận bản chất."),
    ("sub", "3. Đối tượng và phạm vi nghiên cứu"),
    ("p", "Đối tượng nghiên cứu là mối quan hệ giữa kết quả đo hoạt tính (với tư cách là hiện tượng) và "
          "cơ chế tác dụng của hợp chất (với tư cách là bản chất) trong nghiên cứu hợp chất thiên nhiên. "
          "Phạm vi nghiên cứu được giới hạn ở giai đoạn đánh giá tiền lâm sàng sớm, gồm các phép thử ức "
          "chế enzyme *in vitro* và mô phỏng docking phân tử; các vấn đề của thử nghiệm lâm sàng chỉ được "
          "đề cập ở mức liên hệ."),
    ("sub", "4. Phương pháp nghiên cứu"),
    ("p", "Tiểu luận dựa trên thế giới quan duy vật biện chứng và phương pháp luận biện chứng duy vật; sử "
          "dụng các phương pháp phân tích và tổng hợp, lôgíc và lịch sử, đi từ trừu tượng đến cụ thể; kết "
          "hợp với phương pháp tổng quan tài liệu khoa học chuyên ngành hóa dược, hóa sinh và hóa học hợp "
          "chất thiên nhiên."),
    ("sub", "5. Kết cấu của tiểu luận"),
    ("p", "Ngoài Phần mở đầu, Kết luận và Danh mục tài liệu tham khảo, tiểu luận gồm ba chương. Chương 1 "
          "trình bày nội dung của cặp phạm trù bản chất và hiện tượng cùng ý nghĩa phương pháp luận của "
          "nó. Chương 2 phân tích thực trạng sai lệch giữa hiện tượng hoạt tính và bản chất tác dụng "
          "trong đánh giá hoạt tính ức chế enzyme của hợp chất thiên nhiên. Chương 3 vận dụng cặp phạm "
          "trù này để đề xuất các nguyên tắc và một quy trình đánh giá."),

    # --------------------------------------------------------------- CHƯƠNG 1
    ("h1", "CHƯƠNG 1\nNỘI DUNG CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG TRONG PHÉP BIỆN CHỨNG DUY VẬT",
     "CHƯƠNG 1. NỘI DUNG CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG TRONG PHÉP BIỆN CHỨNG DUY VẬT"),
    ("h2", "1.1. Phạm trù và vị trí của cặp phạm trù bản chất – hiện tượng"),
    ("p", "Phạm trù là những khái niệm rộng nhất, phản ánh những mặt, những thuộc tính, những mối liên hệ "
          "chung, cơ bản nhất của các sự vật và hiện tượng thuộc một lĩnh vực nhất định [2]. Mỗi khoa học "
          "cụ thể có hệ thống phạm trù riêng; chẳng hạn, “liên kết hóa học”, “cơ chế phản ứng”, “ái lực "
          "gắn kết” là các phạm trù của hóa học và hóa sinh, phản ánh các mối liên hệ trong một lĩnh vực "
          "hiện thực xác định. Phạm trù của phép biện chứng duy vật có phạm vi rộng hơn: chúng phản ánh "
          "những mối liên hệ phổ biến nhất, có mặt trong tự nhiên, xã hội và tư duy [1], [2]. Phạm trù có "
          "tính khách quan về nội dung, vì nội dung của nó là sự phản ánh những mối liên hệ tồn tại khách "
          "quan; đồng thời có tính chủ quan về hình thức, vì nó là sản phẩm của tư duy trừu tượng. Hệ thống "
          "phạm trù không khép kín mà được bổ sung, điều chỉnh cùng với sự phát triển của thực tiễn và của "
          "nhận thức khoa học."),
    ("p", "Phép biện chứng duy vật khái quát sáu cặp phạm trù cơ bản: cái riêng và cái chung; nguyên nhân "
          "và kết quả; tất nhiên và ngẫu nhiên; nội dung và hình thức; bản chất và hiện tượng; khả năng và "
          "hiện thực. Các cặp phạm trù này cụ thể hóa hai nguyên lý cơ bản (nguyên lý về mối liên hệ phổ "
          "biến và nguyên lý về sự phát triển) và bổ sung cho ba quy luật cơ bản của phép biện chứng, song "
          "mỗi cặp phản ánh một phương diện riêng của các mối liên hệ [2]. Cặp phạm trù bản chất và hiện "
          "tượng phản ánh quan hệ giữa mặt bên trong, tương đối ổn định, quy định sự vận động của sự vật "
          "với mặt bên ngoài, biến đổi, có thể quan sát trực tiếp. Do liên quan trực tiếp đến sự chuyển "
          "hóa từ nhận thức cảm tính lên nhận thức lý tính, cặp phạm trù này có ý nghĩa đặc biệt đối với "
          "nhận thức luận và phương pháp luận của các khoa học thực nghiệm, trong đó có hóa học."),
    ("h2", "1.2. Khái niệm bản chất, hiện tượng và giả tượng"),
    ("p", "Trong lịch sử triết học, quan hệ giữa bản chất và hiện tượng được giải quyết theo những cách "
          "khác nhau. Chủ nghĩa duy tâm chủ quan có xu hướng phủ nhận sự tồn tại khách quan của bản chất, "
          "coi đó chỉ là tên gọi hoặc là tổ hợp của các cảm giác. I. Kant thừa nhận sự tồn tại khách quan "
          "của “vật tự nó” nhưng cho rằng con người chỉ nhận thức được hiện tượng, còn bản chất của vật tự "
          "nó thì không thể nhận thức được. Một số trào lưu thực chứng chủ trương khoa học chỉ cần mô tả "
          "hiện tượng, không cần truy tìm bản chất. G.W.F. Hegel đặt vấn đề một cách biện chứng khi cho "
          "rằng bản chất phải biểu hiện ra và hiện tượng là sự biểu hiện của bản chất, song ông quy cả hai "
          "về sự vận động của “ý niệm tuyệt đối” [1], [2]."),
    ("p", "Trên lập trường duy vật biện chứng, **bản chất** là tổng thể các mặt, các mối liên hệ tất nhiên, "
          "tương đối ổn định ở bên trong sự vật, quy định sự vận động và phát triển của sự vật đó; **hiện "
          "tượng** là sự biểu hiện ra bên ngoài của những mặt, những mối liên hệ ấy trong những điều kiện "
          "xác định [2]. Bản chất và hiện tượng đều tồn tại khách quan, không phụ thuộc vào ý thức của con "
          "người. Bản chất gắn liền với cái chung và cùng trình độ với quy luật: nói đến bản chất là nói "
          "đến cái tất nhiên, lặp lại trong những điều kiện nhất định. Tuy vậy, bản chất rộng hơn quy luật, "
          "vì một bản chất có thể bao hàm nhiều quy luật [1]."),
    ("p", "Cần phân biệt hiện tượng với **giả tượng**. Giả tượng cũng là hiện tượng khách quan, nhưng biểu "
          "hiện bản chất dưới dạng xuyên tạc, khiến người quan sát, nếu dừng lại ở bề mặt, gán cho sự vật "
          "một bản chất mà nó không có. Giả tượng không phải là ảo giác chủ quan; nó phát sinh từ chính các "
          "điều kiện khách quan trong đó bản chất được biểu hiện [1], [2]. Như sẽ phân tích ở Chương 2, "
          "nhiều “hoạt tính” được ghi nhận trong thử nghiệm sinh học thuộc loại giả tượng: tín hiệu đo là "
          "có thật, nhưng nguyên nhân của nó không phải là cơ chế mà người nghiên cứu gán cho hợp chất."),
    ("p", "Quan hệ này có thể minh họa bằng một ví dụ hóa học quen thuộc. Tính acid của một dung dịch biểu "
          "hiện ra qua giá trị pH đo được, màu của chất chỉ thị hay tốc độ phản ứng với kim loại; đó là "
          "những hiện tượng. Bản chất của tính acid là khả năng cho proton, được quy định bởi cấu trúc "
          "electron và độ bền của base liên hợp, thể hiện định lượng qua hằng số pK_{a}. Cùng một bản chất "
          "có thể biểu hiện thành những hiện tượng khác nhau tùy dung môi, nồng độ và nhiệt độ; ngược lại, "
          "cùng một hiện tượng (một giá trị pH) có thể xuất phát từ những bản chất khác nhau, chẳng hạn "
          "một acid mạnh ở nồng độ thấp và một acid yếu ở nồng độ cao."),
    ("h2", "1.3. Mối quan hệ biện chứng giữa bản chất và hiện tượng"),
    ("h3", "1.3.1. Sự thống nhất giữa bản chất và hiện tượng"),
    ("p", "Bản chất và hiện tượng thống nhất với nhau: bản chất bao giờ cũng bộc lộ ra thông qua hiện "
          "tượng, còn hiện tượng bao giờ cũng là sự biểu hiện của một bản chất nhất định. Không có bản chất "
          "thuần túy tồn tại tách rời hiện tượng, cũng không có hiện tượng hoàn toàn không biểu hiện bản "
          "chất. V.I. Lênin viết: “Bản chất hiện ra. Hiện tượng là có tính bản chất” [3]. Sự thống nhất "
          "còn thể hiện ở chỗ bản chất và hiện tượng về căn bản phù hợp với nhau: bản chất nào thì hiện "
          "tượng ấy; khi bản chất thay đổi thì hiện tượng biểu hiện nó cũng thay đổi theo; khi bản chất mất "
          "đi thì hiện tượng tương ứng cũng mất đi [2]. Chính sự thống nhất này là cơ sở khách quan cho "
          "khả năng nhận thức bản chất thông qua việc nghiên cứu hiện tượng."),
    ("h3", "1.3.2. Sự đối lập giữa bản chất và hiện tượng"),
    ("p", "Sự thống nhất giữa bản chất và hiện tượng là sự thống nhất của các mặt đối lập. Thứ nhất, bản "
          "chất phản ánh cái chung, cái tất nhiên, quyết định sự tồn tại của sự vật, còn hiện tượng phản "
          "ánh cái riêng, cái cá biệt. Cùng một bản chất có thể biểu hiện ra thành nhiều hiện tượng khác "
          "nhau tùy theo điều kiện; chẳng hạn, sự chuyển electron trong phản ứng oxy hóa – khử có thể biểu "
          "hiện thành sự đổi màu của dung dịch, sự thoát khí, sự tỏa nhiệt hoặc dòng điện trong pin điện "
          "hóa. Thứ hai, bản chất là mặt bên trong, không thể nhận biết trực tiếp bằng giác quan; hiện "
          "tượng là mặt bên ngoài, có thể quan sát, đo đạc trực tiếp. Thứ ba, bản chất tương đối ổn định, "
          "còn hiện tượng thường xuyên biến đổi. Vì vậy, hiện tượng phong phú hơn bản chất, còn bản chất "
          "sâu sắc hơn hiện tượng [1], [2]."),
    ("p", "Bản chất cũng có nhiều cấp độ. Lênin chỉ ra rằng tư tưởng của con người không ngừng đi sâu từ "
          "hiện tượng đến bản chất, từ bản chất cấp một đến bản chất cấp hai và cứ thế tiếp tục [3]. Như "
          "vậy, nhận thức bản chất là một quá trình, trong đó tri thức đạt được ở mỗi bước là tri thức "
          "tương đối, cần được kiểm nghiệm và đào sâu thêm."),
    ("h2", "1.4. Ý nghĩa phương pháp luận"),
    ("p", "Từ nội dung trên có thể rút ra bốn yêu cầu phương pháp luận, được sử dụng làm cơ sở cho các "
          "phân tích ở Chương 2 và Chương 3."),
    ("p", "*Thứ nhất*, nhận thức không được dừng lại ở hiện tượng mà phải đi đến bản chất. Chỉ khi nắm "
          "được bản chất, con người mới giải thích được đầy đủ các hiện tượng và tác động vào sự vật một "
          "cách có hiệu quả. Trong hoạt động thực tiễn, cần căn cứ vào bản chất chứ không căn cứ vào hiện "
          "tượng để đánh giá sự vật."),
    ("p", "*Thứ hai*, muốn nhận thức bản chất phải xuất phát từ hiện tượng, vì bản chất chỉ bộc lộ qua "
          "hiện tượng. Hơn nữa, cần nghiên cứu nhiều hiện tượng trong nhiều điều kiện khác nhau, vì một "
          "hiện tượng riêng lẻ chỉ phản ánh một phương diện của bản chất."),
    ("p", "*Thứ ba*, cần phân biệt hiện tượng điển hình với giả tượng. Lấy giả tượng làm căn cứ sẽ dẫn "
          "đến kết luận sai về bản chất và do đó dẫn đến hành động sai trong thực tiễn."),
    ("p", "*Thứ tư*, nhận thức bản chất là quá trình đi từ bản chất cấp thấp đến bản chất cấp cao hơn, "
          "gắn với những điều kiện lịch sử – cụ thể; thực tiễn là tiêu chuẩn để kiểm nghiệm mức độ đúng "
          "đắn của tri thức về bản chất."),

    # --------------------------------------------------------------- CHƯƠNG 2
    ("h1", "CHƯƠNG 2\nTHỰC TRẠNG ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME CỦA HỢP CHẤT THIÊN NHIÊN "
           "TỪ GÓC ĐỘ BẢN CHẤT VÀ HIỆN TƯỢNG",
     "CHƯƠNG 2. THỰC TRẠNG ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME CỦA HỢP CHẤT THIÊN NHIÊN "
     "TỪ GÓC ĐỘ BẢN CHẤT VÀ HIỆN TƯỢNG"),
    ("h2", "2.1. Quy trình đánh giá hoạt tính ức chế enzyme và các tầng hiện tượng – bản chất"),
    ("p", "Một nghiên cứu điển hình về hợp chất thiên nhiên gồm các bước: chiết xuất, phân lập bằng các "
          "kỹ thuật sắc ký, xác định cấu trúc bằng phổ cộng hưởng từ hạt nhân (NMR) và khối phổ, sau đó "
          "đánh giá hoạt tính sinh học *in vitro*. Với phép thử ức chế enzyme, hoạt tính được xác định gián "
          "tiếp qua sự thay đổi độ hấp thụ quang hoặc cường độ huỳnh quang của sản phẩm phản ứng. Chẳng "
          "hạn, trong phép thử α-glucosidase phổ biến, enzyme từ nấm men *Saccharomyces cerevisiae* thủy "
          "phân *p*-nitrophenyl-α-D-glucopyranosid (pNPG) tạo thành *p*-nitrophenol, được định lượng qua độ "
          "hấp thụ ở vùng 405 nm; IC_{50} là nồng độ làm giảm 50% tốc độ phản ứng so với mẫu đối chứng. Kết "
          "quả thường được bổ sung bằng mô phỏng docking phân tử để đề xuất cách thức gắn kết của hợp chất "
          "vào tâm hoạt động."),
    ("p", "Xét theo cặp phạm trù bản chất và hiện tượng, quy trình này có cấu trúc nhiều tầng. Hiện tượng "
          "trực tiếp là tín hiệu quang học ghi nhận trên thiết bị. IC_{50} là một hiện tượng đã được xử lý "
          "toán học, phụ thuộc vào nồng độ enzyme, nồng độ cơ chất, thời gian ủ, dung môi hòa tan mẫu và "
          "thành phần dung dịch đệm [12]. Bản chất mà người nghiên cứu cần nhận thức là: hợp chất có gắn kết "
          "đặc hiệu vào enzyme đích hay không, gắn kết theo cơ chế nào, với ái lực bao nhiêu, và tương tác "
          "đó có thể diễn ra trong cơ thể người ở nồng độ đạt được hay không. Giữa hai tầng này không có "
          "sự trùng khớp tự động: cùng một mức giảm tín hiệu có thể xuất phát từ nhiều nguyên nhân khác "
          "nhau, trong đó ức chế đặc hiệu chỉ là một khả năng."),
    ("h2", "2.2. Các dạng giả tượng hoạt tính phổ biến"),
    ("h3", "2.2.1. Ức chế không đặc hiệu do kết tập keo"),
    ("p", "McGovern và cộng sự nghiên cứu 45 hợp chất được xác định là có hoạt tính trong các chiến dịch "
          "sàng lọc thông lượng cao và sàng lọc ảo, và cho thấy 35 hợp chất đồng thời ức chế nhiều enzyme "
          "mô hình không liên quan với nhau. Hoạt tính ức chế này giảm mạnh khi thêm albumin hoặc khi tăng "
          "nồng độ enzyme lên 10 lần; các hợp chất tạo thành những hạt có đường kính 30–400 nm, quan sát "
          "được bằng tán xạ ánh sáng và kính hiển vi điện tử. Trong số đó có quercetin, một flavonoid phổ "
          "biến trong thực vật [17]. Ở nồng độ micromol, các phân tử này tự kết tụ thành hạt keo, hấp phụ "
          "protein và gây ức chế không đặc hiệu [21]. Trong một chiến dịch sàng "
          "lọc 70.563 hợp chất, Feng và cộng sự ghi nhận 1.274 chất ức chế, trong đó 1.204 chất có hoạt "
          "tính nhạy với chất hoạt động bề mặt, tức khoảng 95% số chất có hoạt tính thuộc loại ức chế do "
          "kết tập [14]. Irwin và cộng sự ước tính 5,1% số phối tử được báo cáo có hoạt tính trong khoảng "
          "0,1–10 μM trong tài liệu hóa dược có độ tương đồng cao với các chất kết tập đã biết [15]. Đây là "
          "giả tượng điển hình: sự giảm tín hiệu là có thật, nhưng bản chất của nó là một hiện tượng hóa "
          "lý của hệ keo, không phải tương tác phân tử đặc hiệu như người nghiên cứu mô tả."),
    ("h3", "2.2.2. Hợp chất gây nhiễu đa phép thử và các “thuốc vạn năng” không hợp lệ"),
    ("p", "Baell và Holloway mô tả các nhóm cấu trúc thường xuyên cho kết quả dương tính trong nhiều phép "
          "thử sinh hóa khác nhau và gọi các hợp chất mang chúng là hợp chất gây nhiễu đa phép thử (PAINS) "
          "[7]. Những hợp chất này tạo tín hiệu dương tính thông qua phản ứng cộng hóa trị với protein, chu "
          "trình oxy hóa – khử, tạo phức với ion kim loại, hấp thụ ánh sáng hoặc phát huỳnh quang, thay vì "
          "thông qua gắn kết đặc hiệu với đích [8]. Nhiều khung cấu trúc thuộc nhóm này, như catechol, "
          "quinon và các hệ enon liên hợp, lại phổ biến trong hợp chất thiên nhiên."),
    ("p", "Đối với hợp chất thiên nhiên, Bisson và cộng sự khai thác dữ liệu hơn 80 năm của cơ sở dữ liệu "
          "NAPRALERT và chỉ ra rằng chỉ 39 hợp chất chiếm vị trí nổi bật nhất về tần suất xuất hiện và số "
          "lượng hoạt tính được báo cáo. Tất cả các hợp chất này đều được gán cho rất nhiều hoạt tính khác "
          "nhau, và hơn một nửa không thể giải thích bằng các cơ chế gây nhiễu đã biết đối với thư viện hợp "
          "chất tổng hợp; nhóm tác giả gọi chúng là các “thuốc vạn năng chuyển hóa không hợp lệ” (IMPs) [9]. "
          "Curcumin là trường hợp tiêu biểu: hợp chất này đã được nghiên cứu trong hơn 120 thử nghiệm lâm "
          "sàng, nhưng chưa có thử nghiệm mù đôi, có đối chứng giả dược nào thành công; phân tích hóa dược "
          "cho thấy curcumin kém bền, có khả năng phản ứng và hầu như không có sinh khả dụng [18]. Trong "
          "trường hợp này, sự phong phú của hiện tượng (hoạt tính được ghi nhận trên nhiều mô hình) đã bị "
          "đồng nhất với chiều sâu của bản chất (tác dụng dược lý đặc hiệu)."),
    ("h3", "2.2.3. Sự không tương đồng giữa enzyme mô hình và đích sinh học"),
    ("p", "Oki và cộng sự so sánh tác dụng của các chất ức chế α-glucosidase trên enzyme có nguồn gốc khác "
          "nhau (nấm men bánh mì; ruột non chuột cống, thỏ và lợn). Acarbose, voglibose và "
          "glucono-1,5-lacton ức chế mạnh α-glucosidase của động vật có vú nhưng ức chế yếu hoặc không ức "
          "chế enzyme nấm men; ngược lại, (+)-catechin ức chế tốt enzyme nấm men (IC_{50} = 0,13 mM) nhưng "
          "không làm chậm hoạt tính của enzyme động vật có vú. Phần lớn các mẫu thực phẩm được khảo sát ức "
          "chế enzyme nấm men nhưng không ức chế enzyme của chuột [20]. Kết quả này cho thấy “hoạt tính ức "
          "chế α-glucosidase” xác định trên enzyme nấm men là một hiện tượng gắn với một mô hình cụ thể. "
          "Nếu không kiểm chứng trên enzyme của động vật có vú hoặc của người, việc suy ra tiềm năng điều "
          "trị đái tháo đường type 2 là đồng nhất hiện tượng của mô hình với bản chất của tác dụng trên cơ "
          "thể người. Tương tự, một mẫu thử có IC_{50} thấp hơn acarbose trên enzyme nấm men, hệ mà thuốc "
          "này chỉ ức chế yếu, chưa thể được kết luận là mạnh hơn thuốc điều trị."),
    ("h3", "2.2.4. Tuyệt đối hóa kết quả mô phỏng docking phân tử"),
    ("p", "Điểm số docking không phải là đại lượng đo ái lực gắn kết. Warren và cộng sự đánh giá 10 chương "
          "trình docking và 37 hàm tính điểm trên 8 protein, cho thấy các chương trình có thể tạo tư thế gắn "
          "kết gần với cấu trúc tinh thể (ít nhất với một đích), nhưng không chương trình hay hàm tính điểm "
          "nào dự đoán hữu ích ái "
          "lực gắn kết của phối tử [23]. Khi một giá trị IC_{50} (có thể là giả tượng) được “xác nhận” bằng "
          "một điểm số docking thuận lợi, hai hiện tượng thuộc hai hệ khác nhau được đặt cạnh nhau như thể "
          "cùng chứng minh một bản chất, trong khi mô hình docking đã mặc định trước rằng hợp chất gắn kết "
          "đặc hiệu vào tâm hoạt động, tức là giả định chính điều cần được chứng minh."),
    ("h2", "2.3. Nguyên nhân và hệ quả"),
    ("p", "Sự sai lệch giữa hiện tượng hoạt tính và bản chất tác dụng có nguyên nhân khách quan: tương tác "
          "giữa phân tử nhỏ và enzyme chỉ được nhận biết qua các tín hiệu gián tiếp, chịu tác động của nhiều "
          "yếu tố trong hệ thử; đồng thời nhiều hợp chất thiên nhiên có đặc điểm cấu trúc dễ tạo giả tượng, "
          "như nhiều nhóm hydroxyl phenol, hệ liên hợp và độ ưa mỡ cao [9], [15]."),
    ("p", "Nguyên nhân chủ quan, xét dưới góc độ nhận thức luận, có thể quy về ba dạng sai lầm. Thứ nhất "
          "là đồng nhất một hiện tượng riêng lẻ, như một giá trị IC_{50}, với bản chất tác dụng của hợp chất. "
          "Thứ hai là không phân biệt hiện tượng với giả tượng do thiếu các thí nghiệm đối chứng cần thiết. "
          "Thứ ba là đồng nhất mô hình với đối tượng: coi enzyme nấm men là enzyme đích ở người, hoặc coi "
          "điểm số docking là ái lực gắn kết. Cả ba dạng sai lầm đều vi phạm yêu cầu không dừng lại ở hiện "
          "tượng đã nêu ở mục 1.4. Áp lực công bố kết quả dương tính làm các sai lầm này khó được phát hiện; "
          "biên tập viên nhiều tạp chí của Hiệp hội Hóa học Hoa Kỳ đã ra xã luận chung về vấn đề này, khuyến "
          "nghị tác giả cung cấp bằng chứng thực nghiệm phù hợp khi báo cáo hoạt tính [5]."),
    ("p", "Hệ quả thể hiện ở nhiều cấp độ. Ở cấp độ công trình, nguồn lực bị sử dụng cho những ứng viên "
          "không có tác dụng thực. Ở cấp độ tài liệu khoa học, tỷ lệ hợp chất có đặc điểm giống chất kết "
          "tập trong tài liệu hóa dược đã tăng khoảng 9 lần kể từ năm 1995 [15]. Ở cấp độ phát triển thuốc, "
          "khoảng 90% ứng viên bước vào thử nghiệm lâm sàng không thành công, chủ yếu do thiếu hiệu quả lâm "
          "sàng (40–50%), độc tính không kiểm soát được (khoảng 30%) và tính chất giống thuốc kém (10–15%) "
          "[22]. Tỷ lệ thiếu hiệu quả cao cho thấy khoảng cách đáng kể giữa những gì đo được ở giai đoạn "
          "tiền lâm sàng và tác dụng thực trên người."),

    # --------------------------------------------------------------- CHƯƠNG 3
    ("h1", "CHƯƠNG 3\nVẬN DỤNG CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG NHẰM NÂNG CAO ĐỘ TIN CẬY "
           "CỦA ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME",
     "CHƯƠNG 3. VẬN DỤNG CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG NHẰM NÂNG CAO ĐỘ TIN CẬY "
     "CỦA ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME"),
    ("p", "Bốn yêu cầu phương pháp luận nêu ở mục 1.4 có thể được chuyển thành bốn nguyên tắc cho hoạt động "
          "đánh giá hoạt tính sinh học. Mỗi nguyên tắc dưới đây được cụ thể hóa bằng những thao tác thực "
          "nghiệm có thể kiểm tra được, nhằm tránh việc vận dụng triết học một cách hình thức."),
    ("h2", "3.1. Xuất phát từ hiện tượng: ghi nhận đầy đủ và có kiểm soát"),
    ("p", "Vì bản chất chỉ bộc lộ qua hiện tượng, bước đầu tiên là bảo đảm cho hiện tượng được ghi nhận "
          "đầy đủ, lặp lại được và gắn với điều kiện xác định. Mẫu thử phải có độ tinh khiết được kiểm chứng "
          "bằng phương pháp định lượng như HPLC hoặc qNMR; nếu một tạp chất có hoạt tính mạnh hiện diện với "
          "tỷ lệ nhỏ, hiện tượng ghi nhận được thực chất là hiện tượng của một chất khác. Hoạt tính cần được "
          "xác định bằng đường cong liều – đáp ứng đầy đủ với các lần lặp độc lập, thay cho phần trăm ức chế "
          "tại một nồng độ. Hình dạng đường cong cũng mang thông tin: ức chế do kết tập tương quan với đường "
          "cong có độ dốc lớn bất thường, dù mối tương quan này không tuyệt đối [14], [21]."),
    ("p", "Các điều kiện thử nghiệm cần được báo cáo cụ thể, vì IC_{50} không phải là một hằng số của hợp "
          "chất. Đối với chất ức chế cạnh tranh, phương trình Cheng – Prusoff cho thấy "
          "IC_{50} = K_{i}(1 + [S]/K_{m}), nghĩa là IC_{50} thay đổi theo nồng độ cơ chất [S] được chọn, "
          "trong khi hằng số ức chế K_{i}, đại lượng đặc trưng cho tương tác giữa enzyme và chất ức chế, "
          "không phụ thuộc vào lựa chọn đó [11], [12]. Quan hệ này minh họa trực tiếp luận điểm của phép "
          "biện chứng duy vật: hiện tượng (IC_{50}) biến đổi theo điều kiện, còn bản chất (K_{i}) tương đối "
          "ổn định. Do đó, so sánh IC_{50} giữa các công trình có điều kiện thử nghiệm khác nhau không đủ "
          "giá trị để kết luận về bản chất."),
    ("h2", "3.2. Phân biệt hiện tượng với giả tượng"),
    ("p", "Giả tượng là hiện tượng có thật nhưng biểu hiện bản chất dưới dạng xuyên tạc; vì vậy, không thể "
          "loại bỏ nó bằng cách bác bỏ dữ liệu, mà phải xác định điều kiện khách quan đã sinh ra nó. Đối với "
          "ức chế do kết tập keo, phép kiểm chứng chuẩn là lặp lại phép thử khi có mặt một lượng nhỏ chất "
          "hoạt động bề mặt không ion như Triton X-100; hoạt tính giảm mạnh là dấu hiệu của ức chế do kết "
          "tập [13]. Có thể bổ sung phép thử tăng nồng độ enzyme (hoạt tính của chất kết tập giảm rõ rệt, "
          "còn chất ức chế cạnh tranh điển hình thì không) và phép đo tán xạ ánh sáng động (DLS) để phát "
          "hiện trực tiếp các hạt keo [17]; công cụ “Aggregation Advisor” có thể dùng để cảnh báo sớm [15]. "
          "Đối với nhiễu quang học, cần đo mẫu trắng chứa hợp chất nhưng không chứa enzyme để hiệu chỉnh độ "
          "hấp thụ nội tại, đặc biệt với các hợp chất có màu vàng như nhiều flavonoid. Đối với phản ứng "
          "không đặc hiệu, cần thử trên một enzyme không liên quan và, khi có thể, dùng một phương pháp phát "
          "hiện trực giao. Hoạt tính chỉ xuất hiện trong một hệ đo duy nhất là dấu hiệu hiện tượng phụ thuộc "
          "vào phương pháp đo nhiều hơn là vào tương tác với đích."),
    ("p", "Tuy nhiên, việc nhận diện giả tượng cũng không được thực hiện một cách máy móc. Các cảnh báo "
          "cấu trúc PAINS ban đầu được xây dựng từ sáu phép thử dùng cùng một công nghệ phát hiện; phân tích "
          "dữ liệu công khai của Capuzzi và cộng sự cho thấy 97% hợp chất mang cảnh báo PAINS thực tế hiếm "
          "khi cho kết quả dương tính trong loại phép thử đó, và 87 thuốc phân tử nhỏ đã được FDA phê duyệt "
          "có chứa các cảnh báo này [10]. Một cảnh báo cấu trúc tự nó cũng chỉ là một dấu hiệu bên ngoài; "
          "dùng nó để kết luận thay cho thực nghiệm là lặp lại sai lầm đồng nhất hiện tượng với bản chất, "
          "chỉ theo chiều ngược lại. Kết luận về tính hợp lệ của hoạt tính phải dựa trên các thí nghiệm "
          "trực giao [10]."),
    ("h2", "3.3. Đi từ bản chất cấp một đến bản chất sâu hơn"),
    ("p", "Theo Lênin, nhận thức đi từ bản chất cấp một đến bản chất cấp hai và tiếp tục đi sâu hơn [3]. "
          "Trong đánh giá hoạt tính ức chế enzyme, có thể phân biệt các cấp độ bản chất tương ứng với những "
          "câu hỏi ngày càng sâu. Bản chất cấp một là sự tồn tại của một tác dụng ức chế đặc hiệu, lặp lại "
          "được, sau khi đã loại trừ các giả tượng. Bản chất cấp hai là cơ chế động học của sự ức chế: kiểu "
          "ức chế (cạnh tranh, không cạnh tranh, kháng cạnh tranh hay hỗn hợp), giá trị K_{i}, tính thuận "
          "nghịch và sự phụ thuộc vào thời gian, được xác định bằng các thí nghiệm động học enzyme và thí "
          "nghiệm pha loãng nhanh [12]. Bản chất cấp ba là cấu trúc của phức hợp enzyme – chất ức chế, được "
          "tiếp cận bằng các phương pháp đo liên kết trực tiếp như nhiệt lượng kế chuẩn độ đẳng nhiệt (ITC), "
          "cộng hưởng plasmon bề mặt (SPR), NMR chênh lệch truyền bão hòa (STD-NMR), và ở mức cao nhất là "
          "cấu trúc tinh thể của phức hợp."),
    ("p", "Trong hệ các cấp độ này, docking và mô phỏng động lực học phân tử là mô hình lý thuyết giúp đề "
          "xuất và giải thích cách thức gắn kết, không phải bằng chứng độc lập cho sự tồn tại của hoạt tính. "
          "Mô hình chỉ có giá trị khi nhất quán với dữ liệu thực nghiệm ở các cấp độ thấp hơn: nếu động học "
          "cho thấy kiểu ức chế không cạnh tranh, việc mô tả hợp chất gắn vào tâm hoạt động là mâu thuẫn với "
          "dữ liệu; nếu hợp chất là chất kết tập, mọi tư thế gắn kết được đề xuất đều không có đối tượng "
          "thực. Do các hàm tính điểm không dự đoán hữu ích ái lực gắn kết [23], điểm số docking không nên "
          "được dùng để xếp hạng hoạt tính hoặc để “xác nhận” giá trị IC_{50}."),
    ("p", "Một phương tiện quan trọng để tiếp cận bản chất là quan hệ cấu trúc – hoạt tính (SAR). Khi một "
          "dãy hợp chất tương tự, thu được từ phân lập hoặc bán tổng hợp, có hoạt tính biến đổi một cách có "
          "thể giải thích theo những thay đổi cấu trúc xác định, đó là bằng chứng cho một tương tác đặc hiệu "
          "với vị trí gắn kết. Ngược lại, các hợp chất gây nhiễu thường có SAR “phẳng” hoặc không nhất quán "
          "[17], [21]. Ở đây, cái chung của một dãy hiện tượng (xu hướng SAR) cho phép nhận ra bản chất mà "
          "từng hiện tượng riêng lẻ (một giá trị IC_{50}) không thể chỉ ra. Cuối cùng, chứng minh sự gắn kết "
          "với đích trong môi trường tế bào, chẳng hạn bằng CETSA [16], là bước chuyển từ hệ tinh khiết sang "
          "hệ sinh học phức tạp hơn."),
    ("h2", "3.4. Xem xét hiện tượng trong điều kiện lịch sử – cụ thể và kiểm nghiệm bằng thực tiễn"),
    ("p", "Hiện tượng luôn tồn tại trong những điều kiện cụ thể, và cách thức bản chất bộc lộ ra phụ thuộc "
          "vào các điều kiện đó. Nguyên tắc lịch sử – cụ thể đòi hỏi trước hết phải lựa chọn mô hình thử "
          "nghiệm tương ứng với đích sinh học mà kết luận hướng tới. Nếu mục tiêu là đánh giá khả năng kiểm "
          "soát đường huyết sau ăn, kết quả trên α-glucosidase nấm men chỉ có giá trị sàng lọc sơ bộ; kết "
          "luận cần được kiểm chứng trên α-glucosidase ruột non của động vật có vú hoặc enzyme người tái tổ "
          "hợp, với chất đối chứng dương được đo trong cùng hệ thử [20]."),
    ("p", "Nguyên tắc này cũng đòi hỏi đặt giá trị hoạt tính trong quan hệ với khả năng hợp chất đạt tới "
          "đích trong cơ thể. Một hợp chất có IC_{50} ở mức hàng chục micromol, kém bền trong môi trường sinh "
          "lý và có sinh khả dụng thấp khó tạo ra tác dụng tương ứng *in vivo*, như trường hợp curcumin cho "
          "thấy [18]. Sun và cộng sự lập luận rằng tối ưu hóa thuốc hiện nay chú trọng quá mức vào hiệu lực "
          "và tính đặc hiệu thông qua SAR, trong khi xem nhẹ mức phơi nhiễm và tính chọn lọc ở mô bệnh, và "
          "đề xuất mô hình STAR để phân loại ứng viên [22]. Theo cặp phạm trù đang xét, hiệu lực *in vitro* "
          "là một biểu hiện của bản chất tác dụng nhưng chưa phải toàn bộ bản chất đó; bản chất của tác dụng "
          "dược lý còn bao gồm mối liên hệ giữa phân tử, mô đích và liều dùng."),
    ("p", "Bản thân tri thức về giả tượng hoạt tính cũng có tính lịch sử: ức chế do kết tập được mô tả có "
          "hệ thống năm 2002 [17], cảnh báo PAINS được đề xuất năm 2010 [7], khái niệm IMPs cho hợp chất "
          "thiên nhiên được đưa ra năm 2016 [9], và ngay sau đó giới hạn của cảnh báo PAINS lại được chỉ ra "
          "[10]. Nhận thức về bản chất của “hoạt tính” vì vậy là một quá trình đi sâu liên tục. Thực tiễn, "
          "bao gồm thực nghiệm *in vivo* và thử nghiệm lâm sàng, là tiêu chuẩn cuối cùng để kiểm nghiệm các "
          "kết luận về bản chất tác dụng của một hợp chất."),
    ("h2", "3.5. Quy trình đánh giá theo các cấp độ tiếp cận bản chất"),
    ("p", "Tổng hợp các nguyên tắc trên, có thể đề xuất một quy trình đánh giá hoạt tính ức chế enzyme gồm "
          "sáu cấp độ (Bảng 3.1). Mỗi cấp độ ứng với một câu hỏi về bản chất sâu hơn cấp độ trước và với "
          "những giả tượng cần loại trừ. Kết luận về hoạt tính của một hợp chất cần được phát biểu tương ứng "
          "với cấp độ bằng chứng đã đạt được: chẳng hạn, một hợp chất mới đạt cấp độ 2 nên được mô tả là "
          "“làm giảm hoạt tính enzyme trong điều kiện thử nghiệm”, chưa đủ cơ sở để được gọi là “chất ức "
          "chế đặc hiệu” hay “ứng viên thuốc”."),
    ("table", "BANG_31"),
    ("p", "Quy trình không đòi hỏi mọi nghiên cứu phải đạt cấp độ cao nhất; yêu cầu cốt lõi là sự tương "
          "xứng giữa mức độ khẳng định trong kết luận và cấp độ bằng chứng thu được. Đây là sự vận dụng yêu "
          "cầu “căn cứ vào bản chất chứ không căn cứ vào hiện tượng” vào nghiên cứu hóa học hợp chất thiên "
          "nhiên."),

    # --------------------------------------------------------------- KẾT LUẬN
    ("h1", "KẾT LUẬN", "KẾT LUẬN"),
    ("p", "Cặp phạm trù bản chất và hiện tượng phản ánh mối quan hệ giữa mặt bên trong, tất nhiên, tương "
          "đối ổn định và mặt bên ngoài, biến đổi, có thể quan sát trực tiếp của sự vật. Hai mặt này thống "
          "nhất với nhau, vì bản chất luôn bộc lộ qua hiện tượng và hiện tượng luôn là biểu hiện của bản "
          "chất; đồng thời đối lập với nhau, vì hiện tượng phong phú hơn, bản chất sâu sắc hơn, và hiện "
          "tượng có thể biểu hiện bản chất dưới dạng xuyên tạc (giả tượng). Từ đó, phép biện chứng duy vật "
          "đặt ra yêu cầu nhận thức phải xuất phát từ hiện tượng, phân biệt hiện tượng với giả tượng, không "
          "dừng lại ở hiện tượng mà không ngừng đi vào những cấp độ bản chất sâu hơn, và lấy thực tiễn làm "
          "tiêu chuẩn kiểm nghiệm."),
    ("p", "Vận dụng vào đánh giá hoạt tính ức chế enzyme của hợp chất thiên nhiên, tiểu luận đã chỉ ra "
          "rằng giá trị IC_{50} và điểm số docking thuộc về hiện tượng, trong khi bản chất cần nhận thức là "
          "tương tác đặc hiệu giữa phân tử và đích sinh học cùng khả năng tương tác đó diễn ra trong cơ thể. "
          "Các dạng giả tượng phổ biến gồm ức chế do kết tập keo, hợp chất gây nhiễu đa phép thử, sự không "
          "tương đồng giữa enzyme mô hình và đích sinh học, và việc tuyệt đối hóa kết quả mô phỏng. Nguyên "
          "nhân chủ quan của các sai lệch này là sự đồng nhất hiện tượng với bản chất và đồng nhất mô hình "
          "với đối tượng."),
    ("p", "Trên cơ sở đó, tiểu luận đề xuất bốn nguyên tắc: xuất phát từ hiện tượng được ghi nhận đầy đủ "
          "và có kiểm soát; phân biệt hiện tượng với giả tượng bằng các thí nghiệm trực giao; đi từ bản chất "
          "cấp một đến bản chất sâu hơn thông qua động học enzyme, đo liên kết trực tiếp và quan hệ cấu trúc "
          "– hoạt tính; xem xét hiện tượng trong điều kiện lịch sử – cụ thể và lấy thực tiễn làm tiêu chuẩn. "
          "Các nguyên tắc này được cụ thể hóa thành quy trình sáu cấp độ, với yêu cầu cốt lõi là mức độ "
          "khẳng định trong kết luận phải tương xứng với cấp độ bằng chứng đạt được. Việc vận dụng cũng "
          "đòi hỏi tránh hai khuynh hướng cực đoan: chấp nhận mọi kết quả dương tính như biểu hiện trực "
          "tiếp của bản chất, và loại bỏ máy móc các hợp chất chỉ dựa trên dấu hiệu cấu trúc bên ngoài."),
    ("p", "Đối với bản thân học viên, kết quả của tiểu luận có ý nghĩa định hướng trực tiếp cho việc thiết "
          "kế thí nghiệm trong nghiên cứu hóa học hợp chất thiên nhiên: không dừng lại ở việc báo cáo một "
          "giá trị IC_{50}, mà xây dựng hệ thống bằng chứng nhiều cấp độ, kết hợp phân lập với bán tổng hợp "
          "dẫn xuất để khảo sát quan hệ cấu trúc – hoạt tính, và kiểm chứng trên mô hình phù hợp với đích "
          "sinh học. Tiểu luận mới giới hạn ở các phép thử ức chế enzyme *in vitro*; việc mở rộng phân tích "
          "sang các phép thử trên tế bào và khảo sát định lượng thực trạng công bố trong nước là những hướng "
          "có thể tiếp tục."),
]

# Tài liệu tham khảo: xếp theo ngôn ngữ (tiếng Việt, tiếng Anh), trong mỗi nhóm theo
# thứ tự chữ cái tên tác giả/cơ quan; số thứ tự dùng thống nhất cho trích dẫn trong bài.
TAI_LIEU_VIET = [
    "Bộ Giáo dục và Đào tạo (2015), *Giáo trình Triết học (Dùng cho khối không chuyên ngành Triết học "
    "trình độ đào tạo thạc sĩ, tiến sĩ các ngành khoa học tự nhiên, công nghệ)*, NXB Chính trị quốc gia – "
    "Sự thật, Hà Nội.",
    "Bộ Giáo dục và Đào tạo (2021), *Giáo trình Triết học Mác – Lênin (Dành cho bậc đại học hệ không "
    "chuyên lý luận chính trị)*, NXB Chính trị quốc gia Sự thật, Hà Nội.",
    "V.I. Lênin (2006), *Toàn tập*, tập 29 (Bút ký triết học), NXB Chính trị quốc gia, Hà Nội.",
    "C. Mác và Ph. Ăngghen (1994), *Toàn tập*, tập 25, phần II, NXB Chính trị quốc gia, Hà Nội.",
]

TAI_LIEU_ANH = [
    "Aldrich C., Bertozzi C., Georg G.I., Kiessling L., Lindsley C., Liotta D., Merz K.M., Schepartz A., "
    "Wang S. (2017), “The ecstasy and agony of assay interference compounds”, *Journal of Medicinal "
    "Chemistry*, 60(6), pp. 2165–2168.",
    "Atanasov A.G., Zotchev S.B., Dirsch V.M., International Natural Product Sciences Taskforce, "
    "Supuran C.T. (2021), “Natural products in drug discovery: advances and opportunities”, *Nature Reviews "
    "Drug Discovery*, 20(3), pp. 200–216.",
    "Baell J.B., Holloway G.A. (2010), “New substructure filters for removal of pan assay interference "
    "compounds (PAINS) from screening libraries and for their exclusion in bioassays”, *Journal of "
    "Medicinal Chemistry*, 53(7), pp. 2719–2740.",
    "Baell J., Walters M.A. (2014), “Chemistry: Chemical con artists foil drug discovery”, *Nature*, "
    "513(7519), pp. 481–483.",
    "Bisson J., McAlpine J.B., Friesen J.B., Chen S.-N., Graham J., Pauli G.F. (2016), “Can invalid "
    "bioactives undermine natural product-based drug discovery?”, *Journal of Medicinal Chemistry*, 59(5), "
    "pp. 1671–1690.",
    "Capuzzi S.J., Muratov E.N., Tropsha A. (2017), “Phantom PAINS: Problems with the utility of alerts "
    "for pan-assay interference compounds”, *Journal of Chemical Information and Modeling*, 57(3), "
    "pp. 417–427.",
    "Cheng Y., Prusoff W.H. (1973), “Relationship between the inhibition constant (K_{1}) and the "
    "concentration of inhibitor which causes 50 per cent inhibition (I_{50}) of an enzymatic reaction”, "
    "*Biochemical Pharmacology*, 22(23), pp. 3099–3108.",
    "Copeland R.A. (2013), *Evaluation of Enzyme Inhibitors in Drug Discovery: A Guide for Medicinal "
    "Chemists and Pharmacologists*, 2nd ed., John Wiley & Sons, Hoboken, NJ.",
    "Feng B.Y., Shoichet B.K. (2006), “A detergent-based assay for the detection of promiscuous "
    "inhibitors”, *Nature Protocols*, 1(2), pp. 550–553.",
    "Feng B.Y., Simeonov A., Jadhav A., Babaoglu K., Inglese J., Shoichet B.K., Austin C.P. (2007), “A "
    "high-throughput screen for aggregation-based inhibition in a large compound library”, *Journal of "
    "Medicinal Chemistry*, 50(10), pp. 2385–2390.",
    "Irwin J.J., Duan D., Torosyan H., Doak A.K., Ziebart K.T., Sterling T., Tumanian G., Shoichet B.K. "
    "(2015), “An aggregation advisor for ligand discovery”, *Journal of Medicinal Chemistry*, 58(17), "
    "pp. 7076–7087.",
    "Jafari R., Almqvist H., Axelsson H., Ignatushchenko M., Lundbäck T., Nordlund P., Martinez Molina D. "
    "(2014), “The cellular thermal shift assay for evaluating drug target interactions in cells”, "
    "*Nature Protocols*, 9(9), pp. 2100–2122.",
    "McGovern S.L., Caselli E., Grigorieff N., Shoichet B.K. (2002), “A common mechanism underlying "
    "promiscuous inhibitors from virtual and high-throughput screening”, *Journal of Medicinal "
    "Chemistry*, 45(8), pp. 1712–1722.",
    "Nelson K.M., Dahlin J.L., Bisson J., Graham J., Pauli G.F., Walters M.A. (2017), “The essential "
    "medicinal chemistry of curcumin”, *Journal of Medicinal Chemistry*, 60(5), pp. 1620–1637.",
    "Newman D.J., Cragg G.M. (2020), “Natural products as sources of new drugs over the nearly four "
    "decades from 01/1981 to 09/2019”, *Journal of Natural Products*, 83(3), pp. 770–803.",
    "Oki T., Matsui T., Osajima Y. (1999), “Inhibitory effect of α-glucosidase inhibitors varies "
    "according to its origin”, *Journal of Agricultural and Food Chemistry*, 47(2), pp. 550–553.",
    "Shoichet B.K. (2006), “Screening in a spirit haunted world”, *Drug Discovery Today*, 11(13–14), "
    "pp. 607–615.",
    "Sun D., Gao W., Hu H., Zhou S. (2022), “Why 90% of clinical drug development fails and how to "
    "improve it?”, *Acta Pharmaceutica Sinica B*, 12(7), pp. 3049–3062.",
    "Warren G.L., Andrews C.W., Capelli A.M., Clarke B., LaLonde J., Lambert M.H., Lindvall M., Nevins N., "
    "Semus S.F., Senger S., Tedesco G., Wall I.D., Woolven J.M., Peishoff C.E., Head M.S. (2006), “A "
    "critical assessment of docking programs and scoring functions”, *Journal of Medicinal Chemistry*, "
    "49(20), pp. 5912–5931.",
]
