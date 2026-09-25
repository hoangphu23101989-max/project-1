# -*- coding: utf-8 -*-
"""Chương 3. Thực trạng đánh giá hoạt tính ức chế enzyme của hợp chất thiên nhiên."""

BLOCKS = [
    ("h1", "CHƯƠNG 3\nTHỰC TRẠNG ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME CỦA HỢP CHẤT THIÊN NHIÊN "
           "DƯỚI GÓC ĐỘ CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG",
     "CHƯƠNG 3. THỰC TRẠNG ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME CỦA HỢP CHẤT THIÊN NHIÊN "
     "DƯỚI GÓC ĐỘ CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG"),
    ("p", "Chương này vận dụng các yêu cầu phương pháp luận ở Chương 1 và các bài học nhận thức luận ở Chương "
          "2 để phân tích thực trạng, nguyên nhân và hệ quả của việc đồng nhất hiện tượng với bản chất trong "
          "lĩnh vực này."),

    # ------------------------------------------------------------------ 3.1
    ("h2", "3.1. Hợp chất thiên nhiên và con đường đi đến bản chất của các thuốc ức chế enzyme"),
    ("p", "Nhiều thuốc ức chế enzyme quan trọng có nguồn gốc từ hợp chất thiên nhiên (Bảng 3.1). Điểm chung "
          "của các trường hợp thành công này không phải là một giá trị hoạt tính *in vitro* thấp, mà là việc "
          "quá trình nghiên cứu đã đi qua nhiều cấp độ của bản chất: từ hiện tượng sinh học ban đầu đến cơ "
          "chế, tính chọn lọc, tác dụng trên cơ thể và cuối cùng là hiệu quả lâm sàng."),
    ("table", "B3_1"),
    ("p", "Ngay trong công bố đầu tiên về lipstatin, ngoài giá trị IC_{50} đối với lipase tụy, các tác giả đã "
          "trình bày bằng chứng về tính chọn lọc, về cơ chế ức chế không thuận nghịch gắn với cấu trúc "
          "β-lacton và về tác dụng *in vivo* trên chuột [@weibel1987]. Acarbose được đưa vào điều trị đái tháo "
          "đường type 2 từ năm 1990 sau một quá trình phát triển dài, bao gồm cả công nghệ lên men quy mô lớn "
          "[@wehmeier2004]. Galantamine đi từ tri thức địa phương ở vùng Kavkaz đến sử dụng lâm sàng trong "
          "điều trị bệnh Alzheimer [@heinrich2004]. Sự phát triển các statin gắn liền với việc xác lập mối "
          "quan hệ nhân quả giữa cholesterol máu và bệnh mạch vành [@endo2010]. Captopril được thiết kế trên "
          "cơ sở hiểu biết về cơ chế xúc tác của enzyme đích [@cushman1991]. Như vậy, trong thực tiễn phát "
          "triển thuốc, một hợp chất chỉ trở thành thuốc khi tri thức về nó đã đạt đến những cấp độ bản chất "
          "đủ sâu; khả năng chỉ chuyển thành hiện thực khi hội đủ các điều kiện cần thiết."),

    # ------------------------------------------------------------------ 3.2
    ("h2", "3.2. Quy trình đánh giá hoạt tính ức chế enzyme và cấu trúc hiện tượng – bản chất của nó"),
    ("p", "Một nghiên cứu điển hình về hợp chất thiên nhiên gồm các bước: chiết xuất, phân lập bằng các kỹ "
          "thuật sắc ký, xác định cấu trúc bằng phổ cộng hưởng từ hạt nhân và khối phổ, sau đó đánh giá hoạt "
          "tính sinh học *in vitro*. Với phép thử ức chế enzyme, hoạt tính được xác định gián tiếp qua sự thay "
          "đổi độ hấp thụ quang hoặc cường độ huỳnh quang của sản phẩm phản ứng. Chẳng hạn, trong phép thử "
          "α-glucosidase phổ biến, enzyme từ nấm men *Saccharomyces cerevisiae* thủy phân pNPG tạo thành "
          "*p*-nitrophenol, được định lượng qua độ hấp thụ ở vùng 405 nm; trong phép thử acetylcholinesterase "
          "theo phương pháp Ellman, thiocholin sinh ra phản ứng với DTNB tạo sản phẩm màu vàng được đo ở "
          "412 nm [@ellman1961]. IC_{50} là nồng độ làm giảm 50% tốc độ phản ứng so với mẫu đối chứng. Kết "
          "quả thường được bổ sung bằng mô phỏng docking phân tử để đề xuất cách thức gắn kết của hợp chất "
          "vào tâm hoạt động. Bảng 3.2 tóm tắt một số phép thử thường dùng và những nguy cơ giả tượng đặc "
          "thù của chúng."),
    ("table", "B3_2"),
    ("p", "Xét theo cặp phạm trù bản chất và hiện tượng, quy trình này có cấu trúc nhiều tầng. Hiện tượng trực "
          "tiếp là tín hiệu quang học ghi nhận trên thiết bị; nó được tạo ra thông qua thiết bị đo và phụ "
          "thuộc vào những giả định về phản ứng chỉ thị. IC_{50} là một hiện tượng đã được xử lý toán học, phụ "
          "thuộc vào nồng độ enzyme, nồng độ cơ chất, thời gian ủ, dung môi hòa tan mẫu và thành phần dung "
          "dịch đệm [@copeland2013]. Bản chất mà người nghiên cứu cần nhận thức là: hợp chất có gắn kết đặc "
          "hiệu vào enzyme đích hay không, gắn kết theo cơ chế nào, với ái lực bao nhiêu, và tương tác đó có "
          "thể diễn ra trong cơ thể người ở nồng độ đạt được hay không. Giữa hai tầng này không có sự trùng "
          "khớp tự động: theo cặp phạm trù nguyên nhân – kết quả, cùng một kết quả (mức giảm tín hiệu) có thể "
          "xuất phát từ nhiều nguyên nhân khác nhau, trong đó ức chế đặc hiệu chỉ là một khả năng."),

    # ------------------------------------------------------------------ 3.3
    ("h2", "3.3. Các dạng giả tượng hoạt tính"),
    ("h3", "3.3.1. Ức chế không đặc hiệu do kết tập keo"),
    ("p", "McGovern và cộng sự nghiên cứu 45 hợp chất được xác định là có hoạt tính trong các chiến dịch sàng "
          "lọc thông lượng cao và sàng lọc ảo, và cho thấy 35 hợp chất đồng thời ức chế nhiều enzyme mô hình "
          "không liên quan với nhau. Hoạt tính ức chế này giảm mạnh khi thêm albumin hoặc khi tăng nồng độ "
          "enzyme lên 10 lần, và các hạt kết tập được phát hiện trực tiếp bằng tán xạ ánh sáng. Trong số đó có "
          "quercetin, một flavonoid phổ biến trong thực vật [@mcgovern2002]. Ở nồng độ micromol, các phân tử "
          "này tự kết tụ thành hạt keo, hấp phụ protein và gây ức chế không đặc hiệu [@shoichet2006]. Trong "
          "một chiến dịch sàng lọc 70.563 hợp chất, Feng và cộng sự ghi nhận 1.274 chất ức chế, trong đó 1.204 "
          "chất có hoạt tính nhạy với chất hoạt động bề mặt, tức khoảng 95% số chất có hoạt tính thuộc loại ức "
          "chế do kết tập [@feng2007]. Irwin và cộng sự ước tính 5,1% số phối tử được báo cáo có hoạt tính "
          "trong khoảng 0,1–10 μM trong tài liệu hóa dược có độ tương đồng cao với các chất kết tập đã biết "
          "[@irwin2015]."),
    ("p", "Đây là giả tượng theo đúng nghĩa triết học của khái niệm: sự giảm tín hiệu là có thật và lặp lại "
          "được, nhưng nó biểu hiện xuyên tạc bản chất của quá trình. Bản chất của quá trình ở đây là sự hấp "
          "phụ enzyme lên hạt keo, một quá trình hóa lý của hệ phân tán, không phải tương tác phân tử đặc hiệu "
          "mà người nghiên cứu mô tả. Giả tượng này cũng phát sinh từ điều kiện khách quan (nồng độ, lực ion, "
          "sự vắng mặt của chất hoạt động bề mặt), và do đó chỉ có thể được nhận diện bằng cách thay đổi những "
          "điều kiện ấy, giống như việc chuyển từ hệ hở sang hệ kín trong thí nghiệm của Lavoisier."),
    ("h3", "3.3.2. Hợp chất gây nhiễu đa phép thử và các “thuốc vạn năng” không hợp lệ"),
    ("p", "Baell và Holloway mô tả các nhóm cấu trúc thường xuyên cho kết quả dương tính trong nhiều phép "
          "thử sinh hóa khác nhau và gọi các hợp chất mang chúng là hợp chất gây nhiễu đa phép thử (PAINS) "
          "[@baell2010]. Những hợp chất này tạo tín hiệu dương tính thông qua phản ứng cộng hóa trị với "
          "protein, chu trình oxy hóa – khử, tạo phức với ion kim loại, hấp thụ ánh sáng hoặc phát huỳnh "
          "quang, thay vì thông qua gắn kết đặc hiệu với đích [@baell2014]. Một số nhóm cấu trúc trong danh "
          "mục này, như catechol, quinon và một số hệ enon liên hợp [@baell2010], lại phổ biến trong hợp "
          "chất thiên nhiên."),
    ("p", "Đối với hợp chất thiên nhiên, Bisson và cộng sự khai thác dữ liệu hơn 80 năm của cơ sở dữ liệu "
          "NAPRALERT và xác định 39 hợp chất nổi bật về tần suất xuất hiện và số lượng hoạt tính được báo cáo. "
          "Các hợp chất này đều được gán cho rất nhiều hoạt tính khác nhau, và hơn một nửa không thể giải "
          "thích bằng các cơ chế gây nhiễu đã biết đối với thư viện hợp chất tổng hợp; nhóm tác giả gọi chúng "
          "là các “thuốc vạn năng chuyển hóa không hợp lệ” (IMPs) [@bisson2016]. Curcumin là trường hợp tiêu "
          "biểu: hợp chất này đã được nghiên cứu trong hơn 120 thử nghiệm lâm sàng, nhưng chưa có thử nghiệm "
          "mù đôi, có đối chứng giả dược nào thành công; phân tích hóa dược cho thấy curcumin kém bền, có khả "
          "năng phản ứng và hầu như không có sinh khả dụng [@nelson2017]."),
    ("p", "Trường hợp IMPs là biểu hiện của sự đảo ngược quan hệ giữa hiện tượng và bản chất trong nhận thức. "
          "Phép biện chứng duy vật khẳng định hiện tượng phong phú hơn bản chất; nhưng ở đây, chính sự phong "
          "phú của hiện tượng (hoạt tính được ghi nhận trên hàng trăm mô hình) lại bị coi là bằng chứng cho "
          "chiều sâu của bản chất (tác dụng dược lý đặc hiệu). Trên thực tế, việc một chất “có tác dụng” với "
          "gần như mọi đích là dấu hiệu chứng tỏ cái được đo là một thuộc tính chung, không đặc hiệu của chất "
          "đó, chứ không phải những mối liên hệ tất nhiên với từng đích cụ thể."),
    ("h3", "3.3.3. Sự không tương đồng giữa enzyme mô hình và đích sinh học"),
    ("p", "Oki và cộng sự so sánh tác dụng của các chất ức chế α-glucosidase trên enzyme có nguồn gốc khác "
          "nhau (nấm men bánh mì; ruột non chuột cống, thỏ và lợn). Acarbose, voglibose và glucono-1,5-lacton "
          "ức chế mạnh α-glucosidase của động vật có vú nhưng ức chế yếu hoặc không ức chế enzyme nấm men; "
          "ngược lại, (+)-catechin ức chế tốt enzyme nấm men (IC_{50} = 0,13 mM) nhưng không làm chậm hoạt "
          "tính của enzyme động vật có vú [@oki1999]. Tình trạng tương tự được ghi nhận với tyrosinase: khi "
          "sàng lọc 50.000 hợp chất trên tyrosinase người tái tổ hợp, Mann và cộng sự nhận thấy hydroquinon và "
          "arbutin chỉ ức chế yếu enzyme người, với IC_{50} ở mức milimol; ngược lại, Thiamidol ức chế "
          "tyrosinase người với IC_{50} 1,1 μM nhưng chỉ ức chế yếu tyrosinase nấm (IC_{50} 108 μM). Nhóm tác "
          "giả nhận định phần lớn các chất ức chế tyrosinase đã biết thiếu hiệu quả lâm sàng vì chúng được "
          "phát hiện trên tyrosinase nấm [@mann2018]."),
    ("p", "Những dữ kiện này chứng tỏ “hoạt tính ức chế α-glucosidase” hay “hoạt tính ức chế tyrosinase” được "
          "xác định trên enzyme của nấm men hoặc nấm là một hiện tượng gắn với một mô hình cụ thể. Sai lầm "
          "nhận thức luận ở đây là đồng nhất mô hình với đối tượng: mô hình vốn chỉ phản ánh một số mặt của "
          "đối tượng trong những giới hạn xác định, nhưng lại được coi như chính đối tượng. Tương tự, một mẫu "
          "thử có IC_{50} thấp hơn acarbose trên enzyme nấm men, hệ mà thuốc này chỉ ức chế yếu, chưa thể được "
          "kết luận là mạnh hơn thuốc điều trị. Đây là vi phạm quan điểm lịch sử – cụ thể: tri thức đúng trong "
          "điều kiện này bị chuyển sang điều kiện khác mà không kiểm chứng."),
    ("h3", "3.3.4. Tạp chất và vấn đề đồng nhất của đối tượng nghiên cứu"),
    ("p", "Một tiền đề ngầm của mọi kết luận về hoạt tính là đối tượng được thử chính là hợp chất đã được xác "
          "định cấu trúc. Tiền đề này không phải lúc nào cũng đúng. Hermann và cộng sự phát hiện rằng tạp chất "
          "vô cơ, cụ thể là ion kẽm, trong thư viện hợp chất có thể gây tín hiệu dương tính với nhiều đích và "
          "nhiều hệ đo khác nhau, và đề xuất dùng chất tạo phức TPEN làm phép thử đối chứng [@hermann2013]. "
          "Pauli và cộng sự nhấn mạnh rằng mô tả đúng về một chất đòi hỏi cả cấu trúc lẫn độ tinh khiết, và độ "
          "tinh khiết cần được đánh giá bằng phương pháp trực giao với sắc ký như cộng hưởng từ hạt nhân định "
          "lượng [@pauli2014]. Khi tạp chất có hoạt tính, hiện tượng quan sát được thực chất là biểu hiện của "
          "một sự vật khác; mọi kết luận về bản chất của hợp chất chính khi đó đều mất cơ sở khách quan, vì "
          "nguyên tắc khách quan đã bị vi phạm ngay ở khâu xác định đối tượng được xem xét."),
    ("h3", "3.3.5. Tuyệt đối hóa kết quả mô phỏng docking phân tử"),
    ("p", "Điểm số docking không phải là đại lượng đo ái lực gắn kết. Warren và cộng sự đánh giá 10 chương "
          "trình docking và 37 hàm tính điểm trên 8 protein, cho thấy các chương trình có thể tạo tư thế gắn "
          "kết gần với cấu trúc tinh thể (ít nhất với một đích), nhưng không chương trình hay hàm tính điểm "
          "nào dự đoán hữu ích ái lực gắn kết của phối tử [@warren2006]. Khi một giá trị IC_{50} (có thể là "
          "giả tượng) được “xác nhận” bằng một điểm số docking thuận lợi, hai hiện tượng thuộc hai hệ khác "
          "nhau được đặt cạnh nhau như thể cùng chứng minh một bản chất, trong khi mô hình docking đã mặc định "
          "trước rằng hợp chất gắn kết đặc hiệu vào tâm hoạt động, tức là giả định chính điều cần được chứng "
          "minh. Về mặt lôgíc học, đây là lỗi chứng minh vòng quanh, trong đó luận đề được dùng làm luận cứ "
          "cho chính nó; về mặt nhận thức luận, đây là việc coi một mô hình lý thuyết là sự kiểm nghiệm thực "
          "tiễn."),

    ("h3", "3.3.6. Hoạt tính của dịch chiết: hiện tượng của một tổng thể"),
    ("p", "Trong nhiều nghiên cứu, phép thử hoạt tính được tiến hành trước hết trên dịch chiết thô hoặc các "
          "phân đoạn, và kết quả được dùng để định hướng phân lập. Hoạt tính của một dịch chiết là hiện "
          "tượng của một tổng thể gồm hàng trăm thành phần, trong đó các thành phần có thể tác động độc lập, "
          "cộng hợp, hiệp đồng hoặc đối kháng, và có thể chứa những nhóm chất gây nhiễu phép thử như đã nêu "
          "ở mục 3.3.2 [@bisson2016]. Xét theo nguyên lý về mối liên hệ phổ biến, tổng thể không đơn giản là "
          "tổng các bộ phận: tính chất của tổng thể được quy định bởi cả các bộ phận lẫn mối liên hệ giữa "
          "chúng. Vì vậy, không thể suy trực tiếp từ hoạt tính của dịch chiết ra hoạt tính của một thành "
          "phần được phân lập, cũng không thể coi hợp chất được phân lập với hàm lượng lớn nhất là “hoạt chất” "
          "của dịch chiết chỉ vì nó chiếm ưu thế về lượng."),
    ("p", "Hiện tượng hoạt tính bị mất đi hoặc suy giảm khi phân đoạn, vốn thường gặp trong thực tiễn, cũng "
          "cần được xem xét theo quan điểm này. Nó có thể phản ánh bản chất hiệp đồng của tác dụng, sự phân "
          "hủy của thành phần hoạt tính trong quá trình phân lập, hoặc cho thấy hoạt tính ban đầu là giả tượng "
          "do những chất gây nhiễu tạo ra. Mỗi khả năng đòi hỏi một cách kiểm chứng khác nhau; việc mặc nhiên "
          "chọn một cách giải thích mà không kiểm chứng là vi phạm quan điểm toàn diện, vốn đòi hỏi xem xét sự "
          "vật trong tổng thể các mối liên hệ của nó."),

    # ------------------------------------------------------------------ 3.4
    ("h2", "3.4. Khả năng tái lập của dữ liệu tiền lâm sàng"),
    ("p", "Những giả tượng nêu trên không phải là trường hợp cá biệt. Begley và Ellis cho biết các nhà khoa "
          "học tại công ty Amgen chỉ xác nhận lại được kết quả của 6 trong số 53 công trình tiền lâm sàng "
          "“mang tính bước ngoặt” về ung thư (khoảng 11%) [@begley2012]. Prinz và cộng sự tổng kết 67 dự án "
          "nội bộ của công ty Bayer và cho biết chỉ khoảng 20–25% dự án có dữ liệu công bố hoàn toàn phù hợp "
          "với kết quả kiểm chứng nội bộ [@prinz2011]. Ở cấp độ phát triển thuốc, khoảng 90% ứng viên bước "
          "vào thử nghiệm lâm sàng không thành công, chủ yếu do thiếu hiệu quả lâm sàng (40–50%), độc tính "
          "không kiểm soát được (khoảng 30%) và tính chất giống thuốc kém (10–15%) [@sun2022]."),
    ("p", "Theo phép biện chứng duy vật, bản chất gắn với cái tất nhiên, và quy luật là mối liên hệ bản chất, "
          "tất nhiên, lặp lại trong những điều kiện xác định; do đó, tính lặp lại là một dấu hiệu của bản "
          "chất. Một kết quả không lặp lại được khi kiểm chứng độc lập, hoặc mất đi khi điều kiện thay đổi "
          "không đáng kể, là dấu hiệu nó gắn với những yếu tố ngẫu nhiên, cá biệt của một hệ thí nghiệm cụ "
          "thể, tức là thuộc về hiện tượng chứ chưa phải bản chất. Tỷ lệ tái lập thấp vì vậy không chỉ là vấn "
          "đề kỹ thuật, mà là biểu hiện ở quy mô lớn của việc đồng nhất hiện tượng với bản chất."),

    # ------------------------------------------------------------------ 3.5
    ("h2", "3.5. Nguyên nhân của sự sai lệch giữa hiện tượng và bản chất"),
    ("h3", "3.5.1. Nguyên nhân khách quan"),
    ("p", "Nguyên nhân khách quan nằm ở chính mối quan hệ giữa bản chất và hiện tượng trong lĩnh vực này. "
          "Tương tác giữa phân tử nhỏ và enzyme không thể quan sát trực tiếp mà chỉ được nhận biết qua các "
          "tín hiệu gián tiếp, chịu tác động của nhiều yếu tố trong hệ thử. Nhiều hợp chất thiên nhiên có đặc "
          "điểm cấu trúc dễ tạo giả tượng, như nhiều nhóm hydroxyl phenol, hệ liên hợp và độ ưa mỡ cao "
          "[@bisson2016; @irwin2015]. Mẫu phân lập từ tự nhiên có thể chứa những lượng nhỏ các chất có hoạt "
          "tính mạnh hơn chính hợp chất chính [@pauli2014]. Ngoài ra, các enzyme sẵn có trên thị trường với "
          "giá thành thấp thường có nguồn gốc từ vi sinh vật hoặc động vật, không phải enzyme người."),
    ("h3", "3.5.2. Nguyên nhân chủ quan từ góc độ nhận thức luận"),
    ("p", "Nguyên nhân chủ quan có thể quy về bốn dạng sai lầm nhận thức luận. *Thứ nhất*, đồng nhất một hiện "
          "tượng riêng lẻ, như một giá trị IC_{50}, với bản chất tác dụng của hợp chất; đây là biểu hiện của "
          "bệnh kinh nghiệm. *Thứ hai*, không phân biệt hiện tượng với giả tượng do thiếu các thí nghiệm đối "
          "chứng cần thiết. *Thứ ba*, đồng nhất mô hình với đối tượng: coi enzyme nấm men là enzyme đích ở "
          "người, hoặc coi điểm số docking là ái lực gắn kết. *Thứ tư*, theo chiều ngược lại, áp dụng máy móc "
          "các quy tắc hình thức, chẳng hạn loại bỏ một hợp chất chỉ vì nó mang một nhóm cấu trúc bị cảnh báo; "
          "đây là biểu hiện của bệnh giáo điều. Cả bốn dạng sai lầm đều vi phạm các yêu cầu phương pháp luận "
          "đã nêu ở mục 1.7 và đều bắt nguồn từ phương pháp tư duy siêu hình, hoặc đồng nhất, hoặc tách rời "
          "bản chất và hiện tượng."),
    ("p", "Phương pháp tư duy siêu hình biểu hiện ở đây qua ba đặc trưng. *Thứ nhất*, xem xét sự vật trong "
          "trạng thái cô lập: giá trị IC_{50} được tách khỏi những điều kiện đã sinh ra nó và được coi như một "
          "thuộc tính cố hữu của hợp chất. *Thứ hai*, xem xét sự vật trong trạng thái tĩnh tại: một kết quả ở "
          "cấp độ hiện tượng được coi là kết luận cuối cùng, thay vì là điểm xuất phát của quá trình nhận thức. "
          "*Thứ ba*, tư duy theo lối “hoặc là – hoặc là”: một hợp chất hoặc được coi là “có hoạt tính”, hoặc bị "
          "loại bỏ hoàn toàn, mà không thấy các cấp độ trung gian của bằng chứng. Khắc phục những đặc trưng "
          "này là nội dung của việc vận dụng phép biện chứng duy vật vào hoạt động nghiên cứu."),
    ("h3", "3.5.3. Điều kiện xã hội của hoạt động nghiên cứu"),
    ("p", "Nhận thức khoa học là một hoạt động xã hội, chịu sự chi phối của những điều kiện xã hội cụ thể. Áp "
          "lực công bố và xu hướng ưu tiên kết quả dương tính khiến những kết quả chưa được kiểm chứng đầy đủ "
          "dễ được đưa vào tài liệu khoa học. Biên tập viên nhiều tạp chí của Hiệp hội Hóa học Hoa Kỳ đã ra xã "
          "luận chung, yêu cầu tác giả phân tích khả năng gây nhiễu và, với hợp chất có nguy cơ này, chứng "
          "minh hoạt tính bằng ít nhất hai phép thử khác nhau [@aldrich2017]. Những biện pháp này cho thấy "
          "việc khắc phục sai lầm nhận thức không chỉ phụ thuộc vào năng lực của từng nhà nghiên cứu, mà còn "
          "phụ thuộc vào các chuẩn mực tập thể của cộng đồng khoa học."),

    # ------------------------------------------------------------------ 3.6
    ("h2", "3.6. Hệ quả"),
    ("p", "Hệ quả của sự đồng nhất hiện tượng với bản chất thể hiện ở ba cấp độ. Ở cấp độ từng công trình, "
          "nguồn lực bị dùng cho những ứng viên không có tác dụng thực. Ở cấp độ tài liệu khoa học, dữ liệu "
          "không hợp lệ tích lũy dần: tỷ lệ hợp chất có đặc điểm giống chất kết tập trong tài liệu hóa dược đã "
          "tăng khoảng 9 lần kể từ năm 1995 [@irwin2015]; những dữ liệu này lại trở thành tiền đề cho các "
          "nghiên cứu tiếp theo, làm cho sai lầm được lặp lại và tích lũy. Ở cấp độ phát triển thuốc, khoảng "
          "cách giữa kết quả tiền lâm sàng và tác dụng thực trên người làm tăng tỷ lệ thất bại lâm sàng "
          "[@sun2022]. Xét theo quan hệ giữa lý luận và thực tiễn, đây là trường hợp lý luận (tri thức về hoạt "
          "tính) không được thực tiễn kiểm nghiệm đầy đủ trước khi được dùng để định hướng thực tiễn."),

    ("sub", "Tiểu kết Chương 3"),
    ("p", "Chương 3 đã chỉ ra rằng trong đánh giá hoạt tính ức chế enzyme của hợp chất thiên nhiên, giá trị "
          "IC_{50} và điểm số docking thuộc về hiện tượng, còn bản chất cần nhận thức là tương tác đặc hiệu "
          "giữa phân tử và đích sinh học cùng khả năng tương tác đó diễn ra trong cơ thể. Các giả tượng hoạt "
          "tính phát sinh từ điều kiện khách quan của phép thử và chỉ được nhận diện khi các điều kiện ấy được "
          "thay đổi có kiểm soát. Nguyên nhân chủ quan của việc đồng nhất hiện tượng với bản chất là phương "
          "pháp tư duy siêu hình, biểu hiện dưới hai dạng đối lập là bệnh kinh nghiệm và bệnh giáo điều."),
]
