# -*- coding: utf-8 -*-
"""Chương 4. Vận dụng cặp phạm trù bản chất và hiện tượng."""

BLOCKS = [
    ("h1", "CHƯƠNG 4\nVẬN DỤNG CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG NHẰM NÂNG CAO ĐỘ TIN CẬY "
           "CỦA ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME",
     "CHƯƠNG 4. VẬN DỤNG CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG NHẰM NÂNG CAO ĐỘ TIN CẬY "
     "CỦA ĐÁNH GIÁ HOẠT TÍNH ỨC CHẾ ENZYME"),
    ("p", "Vận dụng triết học vào một lĩnh vực khoa học cụ thể không có nghĩa là thay thế các phương pháp "
          "chuyên ngành bằng các luận điểm triết học, mà là chỉ ra cơ sở phương pháp luận chung của các "
          "phương pháp ấy, từ đó định hướng việc lựa chọn, kết hợp và diễn giải chúng. Theo tinh thần đó, "
          "bốn yêu cầu phương pháp luận nêu ở mục 1.7 được chuyển thành bốn nguyên tắc cho hoạt động đánh giá "
          "hoạt tính sinh học. Mỗi nguyên tắc được cụ thể hóa bằng những thao tác thực nghiệm có thể kiểm tra "
          "được, nhằm tránh việc vận dụng triết học một cách hình thức, và được đặt trong liên hệ với các "
          "nguyên tắc phương pháp luận chung của phép biện chứng duy vật."),

    # ------------------------------------------------------------------ 4.1
    ("h2", "4.1. Nguyên tắc thứ nhất: xuất phát từ hiện tượng được ghi nhận đầy đủ và có kiểm soát"),
    ("p", "Nguyên tắc này là sự cụ thể hóa của nguyên tắc khách quan: xuất phát từ bản thân sự vật, không "
          "lấy ý muốn chủ quan thay cho hiện thực. Vì bản chất chỉ bộc lộ qua hiện tượng, bước đầu tiên là bảo "
          "đảm cho hiện tượng được ghi nhận đầy đủ, lặp lại được và gắn với điều kiện xác định."),
    ("p", "*Về đối tượng*, mẫu thử phải có độ tinh khiết được kiểm chứng bằng phương pháp định lượng như "
          "HPLC hoặc qNMR [@pauli2014]; nếu một tạp chất có hoạt tính mạnh hiện diện với tỷ lệ nhỏ, hiện "
          "tượng ghi nhận được thực chất là hiện tượng của một chất khác. *Về hiện tượng*, hoạt tính cần được "
          "xác định bằng đường cong liều – đáp ứng đầy đủ với các lần lặp độc lập, thay cho phần trăm ức chế "
          "tại một nồng độ. Hình dạng đường cong cũng mang thông tin: ức chế do kết tập tương quan với đường "
          "cong có độ dốc lớn bất thường, dù mối tương quan này không tuyệt đối [@feng2007; @shoichet2006]."),
    ("p", "*Về điều kiện*, các điều kiện thử nghiệm cần được báo cáo cụ thể, vì IC_{50} không phải là một "
          "hằng số của hợp chất. Đối với chất ức chế cạnh tranh, phương trình Cheng – Prusoff cho thấy "
          "IC_{50} = K_{i}(1 + [S]/K_{m}), nghĩa là IC_{50} thay đổi theo nồng độ cơ chất [S] được chọn, "
          "trong khi hằng số ức chế K_{i}, đại lượng đặc trưng cho tương tác giữa enzyme và chất ức chế, "
          "không phụ thuộc vào lựa chọn đó [@cheng1973; @copeland2013]. Quan hệ này minh họa trực tiếp luận "
          "điểm của phép biện chứng duy vật: hiện tượng (IC_{50}) biến đổi theo điều kiện, còn bản chất "
          "(K_{i}) tương đối ổn định. Do đó, so sánh IC_{50} giữa các công trình có điều kiện thử nghiệm khác "
          "nhau không đủ giá trị để kết luận về bản chất. Hướng dẫn MIABE về thông tin tối thiểu cần báo cáo "
          "đối với một thực thể có hoạt tính sinh học là một công cụ để chuẩn hóa việc ghi nhận hiện tượng "
          "[@orchard2011]."),

    # ------------------------------------------------------------------ 4.2
    ("h2", "4.2. Nguyên tắc thứ hai: phân biệt hiện tượng với giả tượng"),
    ("p", "Nguyên tắc này là sự cụ thể hóa của quan điểm toàn diện: xem xét sự vật trong tổng thể các mối liên "
          "hệ của nó, bao gồm cả mối liên hệ với phương tiện đo và điều kiện đo. Giả tượng là hiện tượng có "
          "thật nhưng biểu hiện bản chất dưới dạng xuyên tạc; vì vậy, không thể loại bỏ nó bằng cách bác bỏ dữ "
          "liệu, mà phải xác định điều kiện khách quan đã sinh ra nó."),
    ("p", "Đối với ức chế do kết tập keo, phép kiểm chứng chuẩn là lặp lại phép thử khi có mặt một lượng "
          "nhỏ chất hoạt động bề mặt không ion như Triton X-100; hoạt tính giảm mạnh là dấu hiệu của ức chế "
          "do kết tập [@feng2006]. Có thể bổ sung phép thử tăng nồng độ enzyme (hoạt tính của chất kết tập "
          "giảm rõ rệt, còn chất ức chế cạnh tranh điển hình thì không) và phép đo tán xạ ánh sáng động để "
          "phát hiện trực tiếp các hạt keo [@mcgovern2002]; công cụ “Aggregation Advisor” có thể được dùng "
          "để cảnh báo sớm [@irwin2015]. Đối với tạp chất kim loại, có thể dùng chất tạo phức TPEN làm phép "
          "thử đối chứng [@hermann2013]. Đối với nhiễu quang học, cần đo mẫu trắng chứa hợp chất nhưng không "
          "chứa enzyme để hiệu chỉnh độ hấp thụ nội tại, đặc biệt với các hợp chất có màu như nhiều "
          "flavonoid. Đối với phản ứng không đặc hiệu, cần thử trên một enzyme không liên quan và, khi có "
          "thể, dùng một phương pháp phát hiện trực giao dựa trên nguyên lý đo khác. Hoạt tính chỉ xuất hiện "
          "trong một hệ đo duy nhất là dấu hiệu hiện tượng phụ thuộc vào phương pháp đo nhiều hơn là vào "
          "tương tác với đích."),
    ("p", "Tuy nhiên, việc nhận diện giả tượng cũng không được thực hiện một cách máy móc. Các cảnh báo cấu "
          "trúc PAINS ban đầu được xây dựng từ sáu phép thử dùng cùng một công nghệ phát hiện; phân tích dữ "
          "liệu công khai của Capuzzi và cộng sự cho thấy 97% hợp chất mang cảnh báo PAINS thực tế hiếm khi "
          "cho kết quả dương tính trong loại phép thử đó, và 87 thuốc phân tử nhỏ đã được FDA phê duyệt có "
          "chứa các cảnh báo này [@capuzzi2017]. Một cảnh báo cấu trúc tự nó chỉ là một dấu hiệu bên ngoài, có "
          "tính xác suất; dùng nó để kết luận thay cho thực nghiệm là lặp lại sai lầm đồng nhất hiện tượng với "
          "bản chất, chỉ theo chiều ngược lại, và là biểu hiện của bệnh giáo điều. Kết luận về tính hợp lệ của "
          "hoạt tính phải dựa trên các thí nghiệm trực giao [@capuzzi2017]."),
    ("p", "Cũng cần lưu ý rằng quan điểm toàn diện không đồng nghĩa với việc đặt mọi dữ kiện ngang hàng nhau. "
          "Chủ nghĩa chiết trung ghép nối một cách máy móc kết quả của nhiều phép thử mà không phân biệt vai "
          "trò của chúng; thuật ngụy biện lựa chọn những dữ kiện có lợi cho giả thuyết và bỏ qua những dữ kiện "
          "bất lợi. Quan điểm toàn diện đòi hỏi xác định những mối liên hệ chủ yếu, có ý nghĩa quyết định đối "
          "với vấn đề đang xét. Trong đánh giá hoạt tính, kết quả của một phép thử trực giao hay của một phép "
          "đối chứng loại trừ giả tượng có giá trị kiểm chứng cao hơn nhiều so với một điểm số docking thuận "
          "lợi; và một kết quả âm tính trong phép đối chứng có thể có sức nặng lớn hơn nhiều kết quả dương "
          "tính lặp lại trong cùng một hệ đo."),

    # ------------------------------------------------------------------ 4.3
    ("h2", "4.3. Nguyên tắc thứ ba: đi từ bản chất cấp một đến bản chất sâu hơn"),
    ("p", "Nguyên tắc này là sự cụ thể hóa của quan điểm phát triển: nhận thức không dừng lại ở một trình độ "
          "đã đạt được mà không ngừng đi sâu. Trong đánh giá hoạt tính ức chế enzyme, có thể phân biệt các cấp "
          "độ bản chất tương ứng với những câu hỏi ngày càng sâu. Bản chất cấp một là sự tồn tại của một tác "
          "dụng ức chế đặc hiệu, lặp lại được, sau khi đã loại trừ các giả tượng. Bản chất cấp hai là cơ chế "
          "động học của sự ức chế: kiểu ức chế (cạnh tranh, không cạnh tranh, kháng cạnh tranh hay hỗn hợp), "
          "giá trị K_{i}, tính thuận nghịch và sự phụ thuộc vào thời gian, được xác định bằng các thí nghiệm "
          "động học enzyme và thí nghiệm pha loãng nhanh [@copeland2013]. Bản chất cấp ba là cấu trúc của phức "
          "hợp enzyme – chất ức chế, được tiếp cận bằng các phương pháp đo liên kết trực tiếp như ITC, SPR, "
          "STD-NMR, và ở mức cao nhất là cấu trúc tinh thể của phức hợp. Trình tự này lặp lại, ở quy mô một "
          "công trình, con đường mà lịch sử động học enzyme đã đi qua (mục 2.5)."),
    ("p", "Trong hệ các cấp độ này, docking và mô phỏng động lực học phân tử là mô hình lý thuyết giúp đề "
          "xuất và giải thích cách thức gắn kết, không phải bằng chứng độc lập cho sự tồn tại của hoạt tính. "
          "Mô hình chỉ có giá trị khi nhất quán với dữ liệu thực nghiệm ở các cấp độ thấp hơn: nếu động học "
          "cho thấy kiểu ức chế không cạnh tranh, việc mô tả hợp chất gắn vào tâm hoạt động là mâu thuẫn với "
          "dữ liệu; nếu hợp chất là chất kết tập, mọi tư thế gắn kết được đề xuất đều không có đối tượng "
          "thực. Do các hàm tính điểm không dự đoán hữu ích ái lực gắn kết [@warren2006], điểm số docking "
          "không nên được dùng để xếp hạng hoạt tính hoặc để “xác nhận” giá trị IC_{50}. Đây là vận dụng "
          "trực tiếp quan điểm về vị trí của mô hình trong nhận thức đã nêu ở mục 1.6.2."),
    ("p", "Một phương tiện quan trọng để tiếp cận bản chất là quan hệ cấu trúc – hoạt tính (SAR). Khi một dãy "
          "hợp chất tương tự, thu được từ phân lập hoặc bán tổng hợp, có hoạt tính biến đổi một cách có thể "
          "giải thích theo những thay đổi cấu trúc xác định, đó là bằng chứng cho một tương tác đặc hiệu với "
          "vị trí gắn kết. Ngược lại, các hợp chất gây nhiễu thường có SAR “phẳng” hoặc không nhất quán "
          "[@mcgovern2002; @shoichet2006]; SAR chặt chẽ được xem là tiêu chí quan trọng nhất để phân biệt hợp "
          "chất gây nhiễu với phối tử thực [@aldrich2017]. Ở đây, theo quan hệ giữa cái chung và cái riêng, "
          "cái chung chỉ tồn tại trong và thông qua cái riêng: xu hướng SAR chỉ bộc lộ qua từng giá trị hoạt "
          "tính riêng lẻ, nhưng cho phép nhận ra bản chất mà không giá trị IC_{50} riêng lẻ nào tự nó chỉ ra "
          "được. Cuối cùng, chứng minh sự gắn kết với đích trong môi trường tế bào, chẳng hạn bằng CETSA "
          "[@jafari2014], là bước chuyển từ hệ tinh khiết sang hệ sinh học phức tạp hơn."),

    # ------------------------------------------------------------------ 4.4
    ("h2", "4.4. Nguyên tắc thứ tư: xem xét hiện tượng trong điều kiện lịch sử – cụ thể và kiểm nghiệm "
           "bằng thực tiễn"),
    ("p", "Nguyên tắc này là sự cụ thể hóa của quan điểm lịch sử – cụ thể và nguyên tắc thống nhất giữa lý "
          "luận và thực tiễn. Hiện tượng luôn tồn tại trong những điều kiện cụ thể, và cách thức bản chất bộc "
          "lộ ra phụ thuộc vào các điều kiện đó. Trước hết, phải lựa chọn mô hình thử nghiệm tương ứng với "
          "đích sinh học mà kết luận hướng tới. Nếu mục tiêu là đánh giá khả năng kiểm soát đường huyết sau "
          "ăn, kết quả trên α-glucosidase nấm men chỉ có giá trị sàng lọc sơ bộ; kết luận cần được kiểm chứng "
          "trên α-glucosidase ruột non của động vật có vú hoặc enzyme người tái tổ hợp, với chất đối chứng "
          "dương được đo trong cùng hệ thử [@oki1999]. Tương tự, kết luận về khả năng làm giảm tăng sắc tố da "
          "cần được kiểm chứng trên tyrosinase người [@mann2018]."),
    ("p", "Nguyên tắc này cũng đòi hỏi đặt giá trị hoạt tính trong quan hệ với khả năng hợp chất đạt tới "
          "đích trong cơ thể. Một hợp chất có IC_{50} ở mức hàng chục micromol, kém bền trong môi trường sinh "
          "lý và có sinh khả dụng thấp khó tạo ra tác dụng tương ứng *in vivo*, như trường hợp curcumin cho "
          "thấy [@nelson2017]. Sun và cộng sự lập luận rằng tối ưu hóa thuốc hiện nay chú trọng quá mức vào "
          "hiệu lực và tính đặc hiệu thông qua SAR, trong khi xem nhẹ mức phơi nhiễm và tính chọn lọc ở mô "
          "bệnh, và đề xuất mô hình STAR để phân loại ứng viên [@sun2022]. Theo cặp phạm trù đang xét, hiệu "
          "lực *in vitro* là một biểu hiện của bản chất tác dụng nhưng chưa phải toàn bộ bản chất đó; bản chất "
          "của tác dụng dược lý còn bao gồm mối liên hệ giữa phân tử, mô đích và liều dùng. Theo cặp phạm trù "
          "khả năng – hiện thực, hoạt tính *in vitro* là khả năng; chỉ khi các điều kiện về phơi nhiễm, tính "
          "chọn lọc và độ an toàn được đáp ứng, khả năng ấy mới có thể chuyển thành hiện thực."),
    ("p", "Bản thân tri thức về giả tượng hoạt tính cũng có tính lịch sử: ức chế do kết tập được mô tả có hệ "
          "thống năm 2002 [@mcgovern2002], cảnh báo PAINS được đề xuất năm 2010 [@baell2010], khái niệm IMPs "
          "cho hợp chất thiên nhiên được đưa ra năm 2016 [@bisson2016], và ngay sau đó giới hạn của cảnh báo "
          "PAINS lại được chỉ ra [@capuzzi2017]. Tiến trình này mang hình thức của phủ định của phủ định: từ "
          "chỗ chấp nhận trực tiếp kết quả phép thử, nhận thức chuyển sang phủ định nó bằng các tiêu chí cấu "
          "trúc; đến lượt mình, việc áp dụng máy móc các tiêu chí cấu trúc bị phủ định khi giới hạn của chúng "
          "được chỉ ra, và nhận thức quay trở lại với kết quả thực nghiệm, nhưng ở trình độ cao hơn, tức là "
          "với hệ thống các thí nghiệm trực giao. Mỗi lần phủ định đều kế thừa yếu tố hợp lý của giai đoạn "
          "trước; nhận thức về bản chất của “hoạt tính” vì vậy là một quá trình đi sâu liên tục. Thực tiễn, "
          "bao gồm thực nghiệm *in vivo* và thử nghiệm lâm sàng, là tiêu chuẩn cuối cùng để kiểm nghiệm các "
          "kết luận về bản chất tác dụng của một hợp chất."),

    # ------------------------------------------------------------------ 4.5
    ("h2", "4.5. Quy trình đánh giá theo các cấp độ tiếp cận bản chất"),
    ("p", "Tổng hợp bốn nguyên tắc trên, có thể đề xuất một quy trình đánh giá hoạt tính ức chế enzyme gồm "
          "sáu cấp độ (Bảng 4.1, Hình 4.1). Mỗi cấp độ ứng với một câu hỏi về bản chất sâu hơn cấp độ trước "
          "và với những giả tượng cần loại trừ. Kết luận về hoạt tính của một hợp chất cần được phát biểu "
          "tương ứng với cấp độ bằng chứng đã đạt được: chẳng hạn, một hợp chất mới đạt cấp độ 2 nên được mô "
          "tả là “làm giảm hoạt tính enzyme trong điều kiện thử nghiệm”, chưa đủ cơ sở để được gọi là “chất "
          "ức chế đặc hiệu” hay “ứng viên thuốc”."),
    ("table", "B4_1"),
    ("figure", "H4_1"),
    ("p", "Quy trình không đòi hỏi mọi nghiên cứu phải đạt cấp độ cao nhất, vì điều đó phụ thuộc vào nguồn "
          "lực và mục tiêu cụ thể. Yêu cầu cốt lõi là sự tương xứng giữa mức độ khẳng định trong kết luận và "
          "cấp độ bằng chứng thu được. Đây là sự vận dụng yêu cầu “căn cứ vào bản chất chứ không căn cứ vào "
          "hiện tượng” vào nghiên cứu hóa học hợp chất thiên nhiên; đồng thời là sự thừa nhận tính tương đối "
          "của chân lý: kết luận ở mỗi cấp độ là đúng trong phạm vi của nó và mở ra khả năng đi tiếp đến cấp "
          "độ sau."),

    # ------------------------------------------------------------------ 4.6
    ("h2", "4.6. Tình huống minh họa"),
    ("p", "Để làm rõ cách vận dụng quy trình, có thể xét một tình huống giả định, được xây dựng cho mục đích "
          "minh họa phương pháp luận, không phải dữ liệu thực nghiệm. Giả sử từ một loài cây thuốc, người "
          "nghiên cứu phân lập được hợp chất X thuộc nhóm flavonol, có nhiều nhóm hydroxyl phenol. Trong phép "
          "thử α-glucosidase nấm men, X cho IC_{50} ở mức micromol thấp, thấp hơn nhiều so với acarbose đo "
          "trong cùng hệ, và mô phỏng docking cho điểm số thuận lợi tại tâm hoạt động của một mô hình enzyme. "
          "Nếu dừng ở đây, người nghiên cứu dễ đi đến kết luận rằng X là “chất ức chế α-glucosidase mạnh hơn "
          "acarbose, có tiềm năng điều trị đái tháo đường”."),
    ("p", "Phân tích theo cặp phạm trù bản chất và hiện tượng cho thấy kết luận đó mới dựa trên hiện tượng "
          "ở cấp độ 2 và trên một mô hình lý thuyết. Hơn nữa, các đặc điểm cấu trúc của X (flavonol, nhiều "
          "nhóm phenol) thuộc về những đặc điểm liên quan đến nguy cơ kết tập và gây nhiễu [@mcgovern2002; "
          "@baell2010], và mô hình enzyme nấm men được biết là cho kết quả khác với enzyme động vật có vú, "
          "trong đó acarbose chỉ ức chế yếu enzyme nấm men [@oki1999]. Áp dụng quy trình ở mục 4.5, người "
          "nghiên cứu sẽ lần lượt kiểm tra độ tinh khiết, lặp lại phép thử khi có chất hoạt động bề mặt, đo "
          "tán xạ ánh sáng động, thử trên α-glucosidase ruột chuột, xác định kiểu ức chế và khảo sát một dãy "
          "dẫn xuất. Bảng 4.2 trình bày ba kịch bản kết quả có thể xảy ra và kết luận được phép rút ra trong "
          "mỗi kịch bản."),
    ("table", "B4_2"),
    ("p", "Điểm quan trọng của tình huống này không nằm ở kịch bản nào sẽ xảy ra, mà ở chỗ trong cả ba kịch "
          "bản, kết luận cuối cùng đều khác với kết luận ban đầu. Ở kịch bản A, cái được coi là biểu hiện của "
          "bản chất thực chất là giả tượng. Ở kịch bản B, hiện tượng là có thật nhưng chỉ tồn tại trong một "
          "điều kiện cụ thể, và việc mở rộng tri thức về nó sang điều kiện khác là vi phạm tính cụ thể của "
          "chân lý. Ở kịch bản C, nhận thức đã tiến đến bản chất cấp hai – cấp ba, nhưng kết luận vẫn phải "
          "giới hạn ở phạm vi đã được kiểm chứng và để ngỏ bước kiểm nghiệm *in vivo*. Như vậy, quy trình "
          "không làm giảm giá trị của nghiên cứu hợp chất thiên nhiên, mà làm cho giá trị ấy được xác lập trên "
          "cơ sở khách quan."),

    # ------------------------------------------------------------------ 4.7
    ("h2", "4.7. Một số kiến nghị"),
    ("p", "Từ những phân tích trên, học viên đề xuất một số kiến nghị đối với hoạt động nghiên cứu và đào "
          "tạo trong lĩnh vực hóa học hợp chất thiên nhiên."),
    ("p", "*Đối với người nghiên cứu*, cần xây dựng quy trình thao tác chuẩn cho các phép thử ức chế enzyme, "
          "trong đó các phép đối chứng loại trừ giả tượng (mẫu trắng không enzyme, chất hoạt động bề mặt, "
          "enzyme đối chứng) là bắt buộc chứ không phải tùy chọn; báo cáo đầy đủ điều kiện thử nghiệm và độ "
          "tinh khiết của mẫu theo tinh thần của hướng dẫn MIABE [@orchard2011]; phân biệt rõ trong văn bản "
          "công bố giữa các thuật ngữ mô tả hiện tượng (“làm giảm tín hiệu”, “ức chế trong điều kiện thử "
          "nghiệm”) và các thuật ngữ khẳng định bản chất (“chất ức chế đặc hiệu”, “cơ chế cạnh tranh”)."),
    ("p", "*Đối với nhóm nghiên cứu và cơ sở đào tạo*, cần kết hợp phân lập với bán tổng hợp dẫn xuất để có "
          "thể khảo sát quan hệ cấu trúc – hoạt tính, qua đó tiến từ hiện tượng riêng lẻ đến cái chung; ưu "
          "tiên sử dụng enzyme có nguồn gốc tương đồng với đích ở người khi kết luận hướng tới ứng dụng điều "
          "trị; đưa nội dung về giả tượng hoạt tính và về vai trò của mô hình trong nhận thức vào chương "
          "trình đào tạo, gắn với môn Triết học, để học viên nhận thức được cơ sở phương pháp luận của các "
          "yêu cầu kỹ thuật."),
    ("p", "*Đối với hoạt động phản biện và biên tập*, cần yêu cầu bằng chứng từ ít nhất hai phép thử độc "
          "lập đối với những hợp chất có nguy cơ gây nhiễu, như các tạp chí của Hiệp hội Hóa học Hoa Kỳ đã "
          "áp dụng [@aldrich2017], đồng thời tránh loại bỏ máy móc các hợp chất chỉ dựa trên cảnh báo cấu "
          "trúc [@capuzzi2017]. Những kiến nghị này thể hiện quan điểm cho rằng việc khắc phục sai lầm nhận "
          "thức đòi hỏi sự thống nhất giữa nỗ lực cá nhân và chuẩn mực tập thể của cộng đồng khoa học."),

    ("h2", "4.8. Ý nghĩa đối với việc rèn luyện tư duy biện chứng của người nghiên cứu"),
    ("p", "Các nguyên tắc và quy trình nêu trên chỉ phát huy tác dụng khi được thực hiện bởi những người "
          "nghiên cứu có tư duy biện chứng. Một quy trình, dù chặt chẽ đến đâu, nếu được thực hiện một cách "
          "hình thức, cũng có thể trở thành một khuôn mẫu giáo điều mới. Chẳng hạn, người nghiên cứu có thể "
          "thực hiện đủ các phép đối chứng nhưng vẫn diễn giải kết quả theo ý muốn, hoặc có thể coi việc hoàn "
          "thành các cấp độ của quy trình là mục đích tự thân, thay vì là phương tiện để nhận thức bản chất."),
    ("p", "Tư duy biện chứng, trong trường hợp này, thể hiện ở ba năng lực. *Một là*, năng lực đặt câu hỏi "
          "về điều kiện của hiện tượng: trước mỗi kết quả, người nghiên cứu cần hỏi kết quả đó được sinh ra "
          "trong những điều kiện nào và nếu điều kiện thay đổi thì nó còn tồn tại hay không. *Hai là*, năng "
          "lực tự phê phán: coi giả thuyết của chính mình là đối tượng cần được kiểm chứng, chủ động tìm kiếm "
          "những dữ kiện có thể bác bỏ nó, và thừa nhận giới hạn của kết luận. *Ba là*, năng lực nhìn nhận "
          "tri thức trong sự vận động: hiểu rằng mỗi kết luận là một chân lý tương đối, vừa có giá trị trong "
          "phạm vi của nó, vừa là tiền đề cho bước nhận thức tiếp theo."),
    ("p", "Việc học tập triết học trong chương trình đào tạo sau đại học vì vậy không chỉ nhằm trang bị kiến "
          "thức lý luận chung, mà còn nhằm hình thành những năng lực tư duy đó. Khi được gắn với những vấn đề "
          "cụ thể của chuyên ngành, như vấn đề giả tượng hoạt tính trong nghiên cứu hợp chất thiên nhiên, các "
          "phạm trù của phép biện chứng duy vật trở thành công cụ trực tiếp của hoạt động nghiên cứu, đúng "
          "với vai trò phương pháp luận của triết học đối với các khoa học cụ thể."),
    ("sub", "Tiểu kết Chương 4"),
    ("p", "Chương 4 đã chuyển bốn yêu cầu phương pháp luận của cặp phạm trù bản chất và hiện tượng thành bốn "
          "nguyên tắc cho hoạt động đánh giá hoạt tính ức chế enzyme, gắn với nguyên tắc khách quan, các quan "
          "điểm toàn diện, phát triển, lịch sử – cụ thể và nguyên tắc thống nhất giữa lý luận và thực tiễn. "
          "Các nguyên tắc này được cụ thể hóa thành quy trình sáu cấp độ, với yêu cầu cốt lõi là mức độ khẳng "
          "định trong kết luận phải tương xứng với cấp độ bằng chứng đạt được. Tình huống minh họa cho thấy "
          "quy trình giúp tránh cả bệnh kinh nghiệm lẫn bệnh giáo điều trong diễn giải kết quả."),
]
